#------------------------------------------------------------
# fin_gpt_main.py
# Purpose: This is the main script of the FinGPT prototype
#          which is intended to assist in the analysis of 
#          stock market equities. 
# Author: T Byorick 2024
# Github link: https://github.com/nbk5876/nbk5876.github.io/tree/5a834f96a425480fac90fa20f881f9dfdc9199cf/GPT_Fin
# Overview: https://aiseattle.chat/FinGPT
#------------------------------------------------------------
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Running fin_gpt_main.py")
from data_fetcher import fetch_financial_data
from data_fetcher import fetch_current_stock_price
from data_structurer import structure_data
from nlp_processor import process_query
from cache_manager import CacheManager
import utils

def main():
    #user_query = input("Enter your financial query: ")
    #user_query = "What is the Price-to-Earnings ratio for Microsoft?"
    user_query = "MSFT"

    print(user_query)

    symbol = 'NTAP'
    symbol = 'SOFI'
    symbol = 'PWR'
    symbol = 'GOVT'
    symbol = 'CPB'
    symbol = 'ASX'
    symbol = 'BA'
    symbol = 'MSFT'
    symbol = 'F'
    
    company_overview_data = fetch_financial_data(symbol)  # Contains P/E ratio, Market Cap, etc.
    current_stock_price = fetch_current_stock_price(symbol)  # Contains the current stock price

    # Combine both data sets into structured_data
    structured_data = {
        "overview": company_overview_data,
        "currentPrice": current_stock_price
    }

    #cache_manager = CacheManager()
    #cached_data = cache_manager.get_cached_data(structured_data)
    
    #if not cached_data:
    response = process_query(user_query, structured_data)
    #   cache_manager.cache_data(structured_data)
    #else:
    #    response = cached_data
    
    print(f"\n{response}")

if __name__ == "__main__":
    main()
