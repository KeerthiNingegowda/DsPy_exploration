import yfinance as yf

TROY_OUNCE_TO_GRAMS = 31.1035

##Note this calculation seems to be off by 5000 to 500 INR per gram. So use it with caution

def get_metal_prices():
    """ Fetch Gold and Silver prices from Yahoo finance. Convert it into INR and return the price per gram
    Note: The yahoo ticker returns the value of purest form of metals available for trading. And in US calculations the quantity is troy ounces.
    """

    metal_tickers = yf.Tickers("GC=F SI=F")
    print(metal_tickers.tickers["GC=F"].fast_info["currency"], metal_tickers.tickers["GC=F"].fast_info["lastPrice"] )
    print(metal_tickers.tickers["SI=F"].fast_info["currency"], metal_tickers.tickers["SI=F"].fast_info["lastPrice"] )

    ##Exchange rate
    inr_rate_usd = yf.Ticker("INR=X").fast_info["lastPrice"]
    print((metal_tickers.tickers["GC=F"].fast_info["lastPrice"] * inr_rate_usd) / TROY_OUNCE_TO_GRAMS) 
    print((metal_tickers.tickers["SI=F"].fast_info["lastPrice"] * inr_rate_usd) / TROY_OUNCE_TO_GRAMS) 


if __name__ == "__main__":
    get_metal_prices()