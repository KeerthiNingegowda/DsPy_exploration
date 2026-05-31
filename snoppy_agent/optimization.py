import dspy
import os
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")

from evals import snoopy_metrics

def create_mipro_optimizer(max_bootstrapped_demos:int=6, max_labeled_demos:int=4):
    prompt_model = dspy.LM("anthropic/claude-sonnet-4-6", api_key=ANTHROPIC_KEY)
    task_model =  dspy.LM("anthropic/claude-haiku-4-5-20251001", api_key=ANTHROPIC_KEY)

    mipro_optimizer = dspy.MIPROv2(
    metric=snoopy_metrics,
    prompt_model=prompt_model,
    task_model=task_model,
    max_bootstrapped_demos=max_bootstrapped_demos,
    max_labeled_demos=max_labeled_demos,
    auto="light",
    init_temperature=0.5)

    return mipro_optimizer