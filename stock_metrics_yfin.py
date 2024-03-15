#------------------------------------------------------------
# stock_metrics_yfin.py
# Purpose: Get stock metrics using yahoo finance methods
# Github Repo: https://github.com/ranaroussi/yfinance
#------------------------------------------------------------
import yfinance as yf
import pprint
import os

def get_yf_stock_metrics(tickers_dict):
    print(f"In get_yf_stock_metrics() \n")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tickers_dict)

    # Initialize the dictionary to store metrics for each ticker
    metrics_dict = {}

    # Loop through the dictionary values to fetch and store the desired metrics
    for company_name, ticker_symbol in tickers_dict.items():    	
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
            'marketCap': info.get('marketCap'),
            'ebitda': info.get('ebitda'),
            'grossMargins': info.get('grossMargins'),
            'bookValue': info.get('bookValue')
        }
    
    #pp.pprint(metrics_dict)

    # Return the dictionary containing metrics for all queried tickers
    return metrics_dict

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    tickers = "KR, COST, GPS"
    metrics = get_yf_stock_metrics(tickers)
    print(f"metrics\n")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(metrics)


