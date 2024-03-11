#------------------------------------------------------------
# yfinance_hello_world.py
# Purpose: 
# Github Repo: https://github.com/ranaroussi/yfinance
#------------------------------------------------------------
import yfinance as yf
import pprint
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Fetching data for a single stock
ticker = yf.Ticker("COST")
msft_info = ticker.info
#print(f"MSFT Ticker {msft_info}")

print(f"\nTicker Info\n")
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(msft_info)

symbol = "KR"
ticker = yf.Ticker(symbol)  # Kroger's ticker symbol is KR
info = ticker.info  # Fetch the ticker information
current_price = info['currentPrice']
print(f"\nCurrent stock price for {symbol}: {current_price}")

def get_my_stock_metrics(tickers):
    # Split the tickers string into a list of individual ticker symbols
    ticker_symbols = tickers.split(", ")
    
    # Initialize the dictionary to store metrics for each ticker
    metrics_dict = {}
    
    # Loop through each ticker symbol to fetch and store the desired metrics
    for ticker_symbol in ticker_symbols:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        
        # Extract and store the specific metrics for the current ticker
        metrics_dict[ticker_symbol] = {
            'currentPrice' : info.get('currentPrice'),
            'earningsGrowth': info.get('earningsGrowth'),
            'revenueGrowth': info.get('revenueGrowth'),
            'dividendYield': info.get('dividendYield'),
            'returnOnEquity': info.get('returnOnEquity'),
            'trailingPE': info.get('trailingPE'),
            'forwardPE': info.get('forwardPE'),
            'debtToEquity': info.get('debtToEquity'),
            'beta': info.get('beta'),
            '52WeekChange': info.get('52WeekChange'),
            'averageVolume': info.get('averageVolume'),
            'marketCap': info.get('marketCap')
        }
    
    # Return the dictionary containing metrics for all queried tickers
    return metrics_dict

# Example usage
tickers = "KR, COST"
metrics = get_my_stock_metrics(tickers)
print(f"metrics\n")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(metrics)
