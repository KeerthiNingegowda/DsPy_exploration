import dspy
import json
import logging
from dotenv import load_dotenv
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

##Load Snoopy tools
from tools import informational, finances, life, utils, learn

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")

#Setup DSPy object
lm = dspy.LM("anthropic/claude-haiku-4-5-20251001", api_key=ANTHROPIC_KEY)
dspy.configure(lm=lm, cache=False)

with open("preferences.json") as f:  ##Change the logic to add base paths to search for.
    logger.info("Loading user preferences data")
    user_preferences = json.load(f)

#Create dspy.Signature for I/O
class SnoopyAgentSignature(dspy.Signature):
    """ You are Snoopy. A personal assistant to me but with constraints. 
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

    user_preferences: dict = dspy.InputField(desc="This is default preferences map. Consists of user preferences and personal context")
    query: str = dspy.InputField(desc="User query or request")
    chat_history : list = dspy.InputField(desc="Chat history for context. You will be given only 10 conversations between system and user for context")
    response: str = dspy.OutputField(desc="Concise and personalized response")


def start_react_agent():

    snoopy_agent = dspy.ReAct(signature=SnoopyAgentSignature, tools = [informational.get_news,
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
        utils.get_todays_date_and_time])
    
    print("Hello! I am Snoppy. How can I help you?")
    messages_hist = list()
    while True:
        query = input().strip()
        if query.lower() == "exit" or query.lower() == "quit":
            break
        messages_hist.append({"role":"user", "content": query})
        res = snoopy_agent(user_preferences=user_preferences, 
                           query=query,
                           chat_history=messages_hist[-10:]) #The most recent 10 chat history
        messages_hist.append({"role":"assisstant", "content":res.response})
        print(dspy.inspect_history(n=1))
        print("\n\n")
        print(res.response)




if __name__ == "__main__":
    start_react_agent()
