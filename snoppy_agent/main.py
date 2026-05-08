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
from tools import informational, finances, life, utils

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")

with open("preferences.json") as f:  ##Change the logic to add base paths to search for.
    logger.info("Loading user preferences data")
    user_preferences = json.load(f)


def start_react_agent():

    ##Just invoke as is one can hook it with agent later
    # news_responses = informational.get_news(user_preferences["news_questions"])
    # print(news_responses)
    # twitter_responses = informational.get_twitter_trends_info(user_preferences["twitter_tavily"][0:5])
    # print(twitter_responses)
    # weather_responses = informational.get_weather_info(user_preferences["weather_location"])
    # print(weather_responses)

    # ##Life tools
    # events = life.fetch_events(user_preferences["days_lookahead"]) ##Should take the default or be directed from user query
    # print(events)

    # #Finances tools
    # metal_prices = finances.get_metal_prices(user_preferences["metal_tickers"])
    # print(metal_prices)
    # stock_prices = finances.get_stock_prices(user_preferences["stock_tickers"], user_preferences["stock_period_of_interest"])
    # print(stock_prices)

    # print(finances.get_creditcard_due_dates(user_preferences["credit_card_bill_due_dates"]))
    # print(finances.get_watchlist_prices(user_preferences["watchlist_items"]))

    print(informational.get_transit_info())


if __name__ == "__main__":
    start_react_agent()
    # print(user_preferences["news_questions"][0:2])
