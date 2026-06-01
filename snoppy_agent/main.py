import dspy
import json
import logging
from dotenv import load_dotenv
import os
from datetime import datetime

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

##Load Snoopy tools
from tools import informational, finances, life, utils, learn

# Evaluator logic
from evals import (
    prep_data,
    build_evaluator,
    ground_truth_for_accuracy_evaluation,
    llm_as_a_judge_accuracy_eval,
)
from datasets import trainset, testset, accuracy_data

# Optimization
import optimization as ot

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")

# Setup DSPy object
lm = dspy.LM("anthropic/claude-haiku-4-5-20251001", api_key=ANTHROPIC_KEY)
dspy.configure(lm=lm, cache=False)

with open("preferences.json") as f:  ##Change the logic to add base paths to search for.
    logger.info("Loading user preferences data")
    user_preferences = json.load(f)


# Create dspy.Signature for I/O
class SnoopyAgentSignature(dspy.Signature):
    """You are Snoopy. A personal assistant to me but with constraints.
    Your role is to take my query, interpret it and then invoke appropriate tools to satisfy the request.
    The user is in Canada. So when presenting web search results always ensure that the domain is in .ca and any measurement results are in metric system.
    Ask any follow-up questions if additional clarity is required.
    Present the contents in a way that is digestible to the user. Sometimes you may be given responses that contain weblinks.
    Also you will be given user preferences to use when invoking tools. Use this as a default preference map. The user can override these preferences during the conversation turns.
    Always preserve the input data type for new preferences such that the tools wont break. For eg:- If a tool recieves a argument that is a list of strings, preserve the data type.

    At a high-level you will access to tools with these themes.
    a) Finances  - Things broadly related to money like credit card bill due dates, any watchlist items, stock prices and metal prices info
    b) Informational - Things brodly related to staying upto date about the world. Example:- news update, twitter trends, weather and transit info
    c) life - Events that you have in calendar that can be birthdays, anniversaries, reminders and other goals.
    d) learning - Helping the user to learn from their favorite podcasts or shows, so that they can decide if it is worth spending time exploring it.
    e) Utility - Gives you info about present date and time

    These are the tools you speciffically have access to:
    a) get_metal_prices - Gets the gold and silver (precious metal) prices from Yahoo Finance.
    b) get_stock_prices - Gets the latest/closed market price for given tickers from Yahoo Finance over a period of x days.
    c) get_creditcard_due_dates - Gets the present date and the upcoming bill due dates so that there is no surprise for the user.
    d) get_watchlist_prices - For a given watchlist items, a tavily search result consisting of information like the product, the price, any associated payment plans and the website link where the purchase can be made will be available.
    e) get_news - Gives a summarized version of responses for topics of interest
    f) get_twitter_trends - For topics of interest fetches latest trends from twitter. Note that this is from Tavily not Twitter itself.
    g) get_weather_info - Gets weather information for cities of interest.
    h) get_transit_info - Gets transit information for a given trip. This may include various modes of transportation, platform numbers or any service alerts.
    i) get_events - Pulls upcoming events in the next X days from Google calendar.
    j) get_todays_date - Gets today's date
    k) get_todays_date_and_time - Gets today's date and time
    l) get_youtube_summaries - Given a channel name, get the channel id(if not available) and other metadata to fetch transcript summaries from the most recent k videos. You will get summaries of the transcript not the raw transcript.

    Use these tools cautiously and be mindful of making duplicate or redundant tool calls as it incurs additional API costs.
    Where applicable for eg: get_metal_prices and get_stock_prices if I am pulling information on a day when markets are closed, use other utility tools to tell me if the markets are closed.
    Ask user for information if you do not have relevant info required to run a task and/or can't infer from the existing information.
    Do not chug tokens like there is no tomorrow. Be mindful about how much content the user can digest.

    When providing response to the user, do not offer action items for which you dont have capabilities for. For eg:- Saying if you want to setup a notification is a capability you dont have yet.
    """

    user_preferences: dict = dspy.InputField(
        desc="This is default preferences map. Consists of user preferences and personal context"
    )
    query: str = dspy.InputField(desc="User query or request")
    chat_history: list = dspy.InputField(
        desc="Chat history for context. You will be given only 10 conversations between system and user for context"
    )
    response: str = dspy.OutputField(desc="Concise and personalized response")


snoopy_agent = dspy.ReAct(
    signature=SnoopyAgentSignature,
    tools=[
        informational.get_news,
        informational.get_twitter_trends_info,
        informational.get_weather_info,
        informational.get_transit_info,
        life.get_events,
        finances.get_metal_prices,
        finances.get_stock_prices,
        finances.get_watchlist_prices,
        finances.get_creditcard_due_dates,
        learn.get_youtube_summaries,
        utils.get_todays_date,
        utils.get_todays_date_and_time,
    ],
)


def start_react_agent():

    """ Start the snoopy agent"""

    print("Hello! I am Snoppy. How can I help you?")
    messages_hist = list()
    while True:
        query = input().strip()
        if query.lower() == "exit" or query.lower() == "quit":
            break
        messages_hist.append({"role": "user", "content": query})
        res = snoopy_agent(
            user_preferences=user_preferences,
            query=query,
            chat_history=messages_hist[-10:],
        )  # The most recent 10 chat history
        print(f"Snoopy's response - {res.response}")
        messages_hist.append({"role": "assistant", "content": res.response})


def evaluate_agent(dataset, fname, pred_module):
    """ Return score on a given dataset"""

    devset = prep_data(dataset, user_preferences)
    evaluator = build_evaluator(devset, fname)
    return evaluator(pred_module)


def optimize_agent(train_data: list, agent_save_path: str):
    """ Tune the dspy.module object using miprov2"""

    mipro = ot.create_mipro_optimizer()
    optimized_snoppy_agent = mipro.compile(student=snoopy_agent, trainset=train_data)

    optimized_snoppy_agent.save(f"./tuning_results/tuned_agents/{agent_save_path}.json")

    return optimized_snoppy_agent


def save_prompt(agent, fname):
    """Save tuned prompts"""

    path = f"./tuning_results/prompts/{fname}.txt"
    with open(path, "w") as f:
        f.write(f"Timestamp: {datetime.now().isoformat()}\n\n")
        for name, predictor in agent.named_predictors():
            f.write(f"=== {name} ===\n")
            f.write(predictor.signature.instructions)
            f.write("\n\n")


def get_snoopy_pred_for_accuracy_eval(agent_module, dataset):
    """Runs LLM as a judge to evalaute content accuracy"""
    results = dict()

    for example in dataset:
        snoopy_response = agent_module(
            user_preferences=user_preferences, query=example["query"], chat_history=[]
        )
        ground_truth = ground_truth_for_accuracy_evaluation(
            example["query"], user_preferences
        )
        judge_response = llm_as_a_judge_accuracy_eval(
            example["query"], ground_truth, snoopy_response.response, user_preferences
        )

        results[example["query"]] = {
            "snoopy_response": snoopy_response.response,
            "ground_truth": ground_truth,
            "judge_score": judge_response[0],
            "judge_reasoning": judge_response[1],
        }

    with open(f"./accuracy_eval/eval1.json", "w") as f:
        json.dump(results, f)


if __name__ == "__main__":
    start_react_agent()
    # baseline_test_result = evaluate_agent(prep_data(testset.testset, user_preferences), "baseline_results_excluded_youtube_examples_final.json", snoopy_agent)
    # save_prompt(snoopy_agent, "baseline_prompt")
    # optimized_snoopy_agent = optimize_agent(prep_data(trainset.trainset, user_preferences),"optimized_snoopy")
    # save_prompt(optimized_snoopy_agent, "optimized_prompt")
    # optimized_test_result = evaluate_agent(prep_data(testset.testset,user_preferences), "tuned_results_excluded_youtube_examples_final.json", optimized_snoopy_agent)
    # print(f"Baseline accuracy on testset - {baseline_test_result}")
    # print(f"Optimized agent accuracy on testset - {optimized_test_result}")
    # get_snoopy_pred_for_accuracy_eval(snoopy_agent, accuracy_data.accuracy_set)
