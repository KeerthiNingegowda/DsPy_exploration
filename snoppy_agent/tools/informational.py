import os
import json
import logging
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_KEY = os.getenv("TAVILY_KEY")
tavily_client = TavilyClient(api_key=TAVILY_KEY)

logger = logging.getLogger(__name__)


##Tool 1 - Get news information
def get_news(news_list: list[str]) -> dict:
    """Gets latest news for the given topics from the last 24 hours.
    Args: news_list - List of user preferred news_topics
    Returns:- A dictoionary of summarized responses for each topic within the news_list
    """
    response = dict()
    logger.info("Fetching the latest news information")
    for news in news_list:
        try:
            search_result = tavily_client.search(
                query=news,
                search_depth="basic",
                topic="news",
                max_results=10,
                days=1,
                include_answer=True,
                include_raw_content=False,
            )
        except Exception as e:
            search_result = str(e)

        response[news] = search_result.get("answer", "No results found")

    return response


## Tool2 - Get info about viral twitter trends by topic_of_interests
# Note - Twitter API is very expsenive hence the substitute
def get_twitter_trends_info(topics: list[str]) -> dict:
    """Gets trends from twitter conditioned by topuc.
    Args:- topics - List of topics of interest
    Returns:- A dictionary consisting key information about the topics and info associated with them
    """

    twitter_response = dict()
    logger.info("Fetching information about twitter topics through Tavily")
    for topic in topics:
        twitter_response[topic] = tavily_client.search(
            query=f"trending Twitter discussions about {topic} today",
            search_depth="basic",
            topic="news",
            max_results=5,
            days=1,
            include_answer=True,
            include_raw_content=False,
        )["answer"]

    return twitter_response


##Tool 3 - Get weather updates - Use tavily again - 
def get_weather_info(cities: list[str]) -> dict:
    """Gets weather info for required cities for the entire day"""

    weather_response = dict()
    logger.info("Getting weather info ")
    for city in cities:
        weather_response[city] = tavily_client.search(
            query=f"Give me the weather forecast info for the entire day today in {city}",
            search_depth="basic",
            topic="general", ##take a note of this
            max_results=1,
            days=1,
            include_answer=True,
            include_raw_content=False,
        )["answer"]
    
    return weather_response


##Tool 4 - Transit-info - Google Maps api
def get_transit_info():
    pass