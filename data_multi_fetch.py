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
    
    symbol_mapping = {
        'Microsoft': 'MSFT',
        'Apple': 'AAPL',
        'Amazon': 'AMZN',
        'Bank of America': 'BAC',
        # ... other mappings ...
    }

    # Return a list of stock symbols for the given company names
    return [symbol_mapping.get(name, 'UNKNOWN') for name in company_names]

# Example usage
if __name__ == "__main__":
    query = "What is your analysis of Microsoft, Apple, NTAP, and Bank of America?"
    symbols = parse_query(query)
    print(symbols)  # This will print the list of stock symbols extracted from the query

