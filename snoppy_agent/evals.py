import dspy
import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")

from datasets import accuracy_data


##For this function, to better understand trace, first try printing trace as is and then backtrack
def extract_tools_from_trace(pred):
    if not hasattr(pred, "trajectory"):
        return []
    tool_names = []
    for key, value in pred.trajectory.items():
        if key.startswith("tool_name_") and value != "finish":
            tool_names.append(value)

    return tool_names

def eval_tool_presence(example:dspy.Example, actual_tools:list) -> float:
    """
    Evaluate if all the required are called to satisfy a given user query and checks if no tools are called for guardrail examples
    """
    if not example.expected_tools:
        return 1.0 if len(actual_tools) == 0 else 0.0
    
    missing = [t for t in example.expected_tools if t not in actual_tools]
    return 1.0 if not missing else 0.0


def ground_truth_for_accuracy_evaluation(query_context:str, user_preferences:dict) -> str:
    """ Function that provides ground truth to evaluate accuracy for subjective and/or unbounded tasks"""

    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.responses.create(
        model="gpt-5.4-mini",
        tools=[{"type":"web_search"}],
        max_output_tokens=600,
        input=f"""Search and find the current accurate information for {query_context}. For referbece you will be given 
        information about user preferences {user_preferences}. Unless the query explicitly asks for information that
    is different than preferences, always refer to this information to know about user interest.
          Return only the factual data you find. Be concise and specific with numbers and dates."""
    )
    return response.output_text


def llm_as_a_judge_accuracy_eval(query:str, ground_truth:str, predicted_response:str, user_preferences:dict, variance:str="2-4%") -> tuple[float,str]:
    """ Return a accuracy score for subjective tasks"""
    prompt = f"""You are evaluating an AI assistant response for factual accuracy for a give query.
    The query is as follows {query}
    Independently verified current information:{ground_truth}
    Agent response to evaluate:{predicted_response}
    You will be given user preference sfor reference {user_preferences}. Unless the query explicitly asks for information that
    is different than preferences, always refer to this information to know about user interest.
    Compare the agent response against the verified information.Allow up to {variance} variance- if testing quantitative values.
    Be lenient on wording, strict on facts.Respond in this exact format. DO NOT add any other text fields:
    Score: <float 0.0 to 1.0>
    Reason: <one sentence>"""

    judge_client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    response = judge_client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[{"role":"user", "content":prompt}]
    )

    output = response.content[0].text.strip()
    try:
        lines = output.split("\n")
        score = float(lines[0].replace("Score:","").strip())
        reason = lines[1].replace("Reason:","").strip()
        return score, reason
    except Exception:
        return 0, "Cannot parse the judge output"

def snoopy_metrics(example, pred, trace=None) -> float:

    """ Aggregate the metrics from all eval functions"""

    actual_tools = extract_tools_from_trace(pred)
    print(actual_tools)
    res = eval_tool_presence(example, actual_tools)
    return res


def prep_data(data:list, user_preferences:dict, chat_history:str="") -> list:
    """ Prepare data for tuning and testing
        Args:-
            data - A list of data examples
        Returns:-
            A list of dspy.Example instances
    """
    return [dspy.Example(d, user_preferences=user_preferences, chat_history=chat_history).with_inputs("query", "user_preferences", "chat_history") for d in data]

def build_evaluator(devset:list, path_to_save:str):
    return dspy.Evaluate(
        devset=devset,
        metric=snoopy_metrics,
        num_threads=1,
        display_progress=True,
        save_as_json=f"./tuning_results/{path_to_save}"
    )
