#------------------------------------------------------------
# data_fetcher.py
# Purpose: Fetch data from one or more financial databases
#          based on the user's query
#------------------------------------------------------------
import os
import requests
from utils import log_error
import json

# Fetch the finacial data
def fetch_financial_data(query):
    print("Running fetch_financial_data")
    ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

    """ --------------------------------------------------------
    Fetch financial data based on the user's query.
    This can be implemented using an API or web scraping methods.
    
    :param query: The user's financial query.
    :return: Raw financial data from the web.
    -------------------------------------------------------------
    """
    # Example implementation using an API
    api_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={query}&apikey={ALPHAVANTAGE_API_KEY}"

    print(f"FINANCIAL FETCH URL is: {api_url}")

    try:
        response = requests.get(api_url, params={'query': query})
        response.raise_for_status()
        data = response.json()

        # Print the entire JSON response as a string for debugging
        print(json.dumps(data, indent=4))

        return data
    except requests.RequestException as e:
        log_error("Error fetching financial data: {}".format(e))
        return None

# Fetch the current stock price
def fetch_current_stock_price(symbol):
    print(f"Running fetch_current_stock_price with: {symbol}")
    api_key = os.getenv('ALPHAVANTAGE_API_KEY')
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["Global Quote"]["05. price"]  # Adjust the key if necessary
    except requests.RequestException as e:
        log_error(f"Error fetching current stock price for {symbol}: {e}")
        return None
