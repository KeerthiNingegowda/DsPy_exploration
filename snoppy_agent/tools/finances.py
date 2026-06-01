import yfinance as yf
from tavily import TavilyClient
from tools import utils
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_KEY = os.getenv("TAVILY_KEY")
tavily_client = TavilyClient(api_key=TAVILY_KEY)

##Taking the exchange rate out of the equation as there is a price difference


def get_metal_prices(tickers: list) -> dict:
    """Fetch Gold and Silver prices from Yahoo finance. The tool can only access information from Yahoo finance.
    Note: The yahoo ticker returns the value of purest form of metals available for trading. And in US calculations the quantity is troy ounces.
    Args:-
        tickers - A list of metal tickers.
    Returns:-
        A dictionary consisting of the ticker symbols and the last trading price
    """

    metal_tickers = yf.Tickers(" ".join(tickers))
    return {
        tickers[
            0
        ]: f"{metal_tickers.tickers[tickers[0]].fast_info["lastPrice"]} - {metal_tickers.tickers[tickers[0]].fast_info["currency"]}",
        tickers[
            1
        ]: f"{metal_tickers.tickers[tickers[1]].fast_info["lastPrice"]} - {metal_tickers.tickers[tickers[1]].fast_info["currency"]}",
    }


def get_stock_prices(stock_tickers: list, period: str) -> dict:
    """Fetch stock prices from Yahoo finance for a given period
    Args:-
        stock_tickers - A list of stock tickers
        period - Number of days to fetch historical results from
    Returns:-
        A dictionary consisting of historical clsoing prices and present market price of input tickers

    """

    hist_result = yf.Tickers(" ".join(stock_tickers)).history(period=period)
    dates = hist_result.index.strftime("%Y-%m-%d").tolist()
    currency_result = yf.Tickers(" ".join(stock_tickers))
    final_currency_list = {
        stock_tickers[idx]: currency_result.tickers[stock_tickers[idx]].fast_info[
            "currency"
        ]
        for idx in range(len(stock_tickers))
    }
    final_results = dict()
    for idx, date in enumerate(dates):
        daily_price = hist_result["Close"].iloc[idx].to_dict()
        final_results[date] = {
            ticker: {"price": f"{round(price,2)} {final_currency_list[ticker]}"}
            for ticker, price in daily_price.items()
        }

    return final_results


def get_creditcard_due_dates(bill_due_info: dict) -> dict:
    """Return credit card bill due dates
    Args:-
        bill_due_info - List of credit cards and their associated due dates.
    Returns:-
        A dictionary consisting of present date and the list of credit cards up for a bill payment
    """

    return {"date_today": utils.get_todays_date(), "credit_card_bill": bill_due_info}


def get_watchlist_prices(watchlist_items: list):
    """Search prices of watchlist items using Tavily search.
    Args:-
        watchlist_items - A liist of items that are of interest
    Returns:-
        A dictionary consisting of item name and associated search results
    """

    watchlist_results = dict()

    for item in watchlist_items:
        item_name = item["item"]
        watchlist_results[item_name] = tavily_client.search(
            query=f"Best price of {item_name}",
            search_depth="basic",
            topic="general",
            include_answer=False,
            max_results=5,
            include_domains=[
                "amazon.ca",
                "bestbuy.ca",
                "walmart.ca",
                "costco.ca",
                "ebay.ca",
                "staples.ca",
                "canadiantire.ca",
            ],
        )
    return watchlist_results
