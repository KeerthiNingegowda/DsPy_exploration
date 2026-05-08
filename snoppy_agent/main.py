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

#Setup DSPy object
lm = dspy.LM("anthropic/claude-haiku-4-5-20251001", api_key=ANTHROPIC_KEY)
dspy.configure(lm=lm, cache=False)

with open("preferences.json") as f:  ##Change the logic to add base paths to search for.
    logger.info("Loading user preferences data")
    user_preferences = json.load(f)

#Create dspy.Signature for I/O
class SnoopyAgentSignature(dspy.Signature):
    """ You are Snooopy. A personal assistant to me but with constraints. Your role is to take my query, interpret it and then invoke appropriate tools to satisfy the request.
        The user is in Canada. So when presenting web search results always ensure that the domain is in .ca and any measurement results are in metric system. 
        Ask any follow-up questions if there is additional clarity is required. Present the contents in a way that is digestible to the user.
        You will be presented with user preferences 

        
        At a high-level you will access tools with these themes.
        a) Finances  - Things broadly related to money like credit card bill due dates, any watchlist items, stock prices and metal prices info 
        b) Informational - Things brodly related to staying upto date. Example:- news update, twitter trends, weather and transit info
        c) life - Events that you have in calendar that can be birthdays, anniversaries, reminders and other goals.
        d) Utility - Gives you info about present date and time
        These are the tools you speciffically have access to:
        a) get_metal_pr
    
    
    """




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
