import yfinance as yf

##Taking the exchange rate out of the equation as there is a price difference

def get_metal_prices(tickers:list) -> tuple:
    """ Fetch Gold and Silver prices from Yahoo finance. Convert it into INR and return the price per gram
    Note: The yahoo ticker returns the value of purest form of metals available for trading. And in US calculations the quantity is troy ounces.
    """

    metal_tickers = yf.Tickers(" ".join(tickers))
    return { tickers[0] : f"{metal_tickers.tickers[tickers[0]].fast_info["lastPrice"]} - {metal_tickers.tickers[tickers[0]].fast_info["currency"]}", 
          tickers[1] : f"{metal_tickers.tickers[tickers[1]].fast_info["lastPrice"]} - {metal_tickers.tickers[tickers[1]].fast_info["currency"]}"
         }
