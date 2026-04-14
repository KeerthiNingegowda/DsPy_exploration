import dspy
from dotenv import load_dotenv
import os 

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")


if __name__ == "__main__":
    print("hello")