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
from tools import informational, finances, life

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")

with open("preferences.json") as f:
    logger.info("Loading user preferences data")
    user_preferences = json.load(f)


def start_react_agent():

    ##Just invoke as is one can hook it with agent later
    # news_responses = informational.get_news(user_preferences["news_questions"])
    # twitter_responses = informational.get_twitter_trends_info(user_preferences["twitter_tavily"][0:5])
    # weather_responses = informational.get_weather_info(user_preferences["weather_location"])
    # print(twitter_responses)

    ##Life tools
    events = life.fetch_events(user_preferences["days_lookahead"]) ##Should take the default or be directed from user query
    print(events)
    # pass


if __name__ == "__main__":
    start_react_agent()
    # print(user_preferences["news_questions"][0:2])
