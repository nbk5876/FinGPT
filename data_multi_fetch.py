#------------------------------------------------------------
# data_multi_fetch.py
# Purpose: Parse NLP queries
# Example queries:
#   NTAP
#   MSFT, Apple, Amazon, CPB
#   What is your analysis of Microsoft?
#   What is your analysis of NTAP?
#   What is your analysis of Microsoft, Apple, NTAP, and Bank of America?
#   How do Nvidia, Advanced Micro Devices, and ARM compare?
#------------------------------------------------------------
import spacy
#from openai import OpenAI
import requests
import os
from utils import print_search_results

print("Running data_multi_fetch.py") 

nlp = spacy.load("en_core_web_sm")  # Example using spaCy

#-------------------------------------------------------
# This is the main function that will be called to parse 
# the user's query
#
#-------------------------------------------------------
def parse_query(query):
    company_names = extract_entities(query)
    return map_name_to_symbol(company_names)

#-------------------------------------------------------
# Use spacy to identify entities
#
#-------------------------------------------------------
def extract_entities(query):
    doc = nlp(query)
    entities = []
    for ent in doc.ents:
        if ent.label_ == "ORG":  # ORG for organizations, GPE for geopolitical entities
            # Here you would have logic to map the entity to a stock symbol
            entities.append(ent.text)
    return entities

#-------------------------------------------------------
# Map extracted company names to their stock symbols.
#-------------------------------------------------------
def map_name_to_symbol(company_names):
    ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
    
    symbol_mapping = {
        'Microsoft': 'MSFT',
        'Apple': 'AAPL',
        'Amazon': 'AMZN',
        'Bank of America': 'BAC',
        # ... other mappings ...
    }

    # call an API for unknown symbols
    for name in company_names:
        if name not in symbol_mapping:

            url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={name}&apikey={ALPHAVANTAGE_API_KEY}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()  # data is a python dictionary
                #print_search_results(data)

                matches = data.get('bestMatches', [])

                # Assuming the best match is the first one in the list
                if matches:
                    # Note: The actual key for the symbol in the API response is "1. symbol"
                    symbol = matches[0].get('1. symbol', None)
                    if symbol:
                        symbol_mapping[name] = symbol
                        continue  # Move on to the next company name once the symbol is found
                        
            # If no symbol is found through the API, mark as 'UNKNOWN'
            symbol_mapping[name] = 'UNKNOWN'

    return [symbol_mapping.get(name, 'UNKNOWN') for name in company_names]

# Example usage
if __name__ == "__main__":
    #query = "What is your analysis of Microsoft, Apple, NTAP, and Bank of America?"
    query = "How do Microsoft, Nvidia, Advanced Micro Devices, ARM Holdings, and Campbell Soup compare?"
    print(query)    # This will print the query

    symbols = parse_query(query)
    print(symbols)  # This will print the list of stock symbols extracted from the query

"""
I'm not sure this approach using spacy is the best approach....  For instance, I gave this question to perplexity:

What are the stock symbols for Microsoft, Nvidia, Advanced Micro Devices, ARM Holdings, and Campbell Soup?

The stock symbols for the requested companies are as follows:
Microsoft: MSFT
Nvidia: NVDA
Advanced Micro Devices: AMD
ARM Holdings: ARMH (Note: ARM Holdings was acquired by NVIDIA in 2020)
Campbell Soup: CPB

Notice that it came back with the correct symbols...
"""