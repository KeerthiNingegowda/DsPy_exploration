import dspy
import numpy as np


##For this function, to better understand trace, first try printing trace as is and then backtrack
def extract_tools_from_trace(trace):
    if not hasattr(trace, "trajectory"):
        return []
    tool_names = []
    for key, value in trace.items():
        if key.startswith("tool_name_") and value != "finish":
            tool_names.append(key)

    return tool_names

def eval_guardrail(example:dspy.Example, tools_called:list) -> float:
    """
    Evaluate if agent violated guardrails. In this case a guardrail is
    invoking an irrelavant tool when it shouldn't be invoked to begin with
    """
    return 1.0 if len(tools_called) == 0 else 0.0

def eval_tool_presence(example:dspy.Example, tools_called:list) -> float:
    """
    Evaluate if all the required are called to satisfy a given user query
    """
    missing = [tool for tool in example.expected_tools if tool not in tools_called]
    return 1.0 if not missing else 0.0
    

def snoopy_metrics(example, pred, trace=None) -> float:

    """ Aggregate the metrics from all eval functions"""
    actual_tools = extract_tools_from_trace(trace)

    guardrail_score = eval_guardrail(example, actual_tools)
    tool_presence_score = eval_tool_presence(example, actual_tools)



    return np.mean([guardrail_score,tool_presence_score])


def prep_data(data:list, user_preferences:dict, chat_history:str="") -> list:
    """ Prepare data for tuning and testing
        Args:-
            data - A list of data examples
        Returns:-
            A list of dspy.Example instances
    """
    return [dspy.Example(**d, user_preferences=user_preferences, chat_history=chat_history).with_inputs("query", "user_preferences", "chat_history") for d in data]

def build_evaluator(devset):
    return dspy.Evaluate(
        devset=devset,
        metric=snoopy_metrics,
        num_threads=1,
        display_progress=True
    )

