#------------------------------------------------------------
# data_symbol_fetch.py
# Purpose: Parse NLP queries
# Example queries:
#   NTAP
#   MSFT, Apple, Amazon, CPB
#   What is your analysis of Microsoft?
#   What is your analysis of NTAP?
#   What is your analysis of Microsoft, Apple, NTAP, and Bank of America?
#   How do Nvidia, Advanced Micro Devices, and ARM compare?
#------------------------------------------------------------
from openai import OpenAI 
from utils import print_search_results, webfile_write


#-------------------------------------------------------
# This is the main function that will be called to parse 
# the user's query
#
#-------------------------------------------------------
def parse_query(query):
    # Initialize the OpenAI client
    client = OpenAI()

    #detailed_description = (
    #    f"What are the stock symbols for Microsoft, Nvidia, Advanced Micro Devices, ARM Holdings, and Campbell Soup?"
    #    + f""
    #)

    detailed_description = (
        f"{query}"
        + f""
    )

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that provides financial analysis."},
            {"role": "user", "content": detailed_description}
        ]
    )

    try:
        response = completion.choices[0].message  # Adjust based on actual response structure
    except IndexError:
        response = "An error occurred processing the query."

    webfile_write('../archive.html', detailed_description, response)

    return response

if __name__ == "__main__":
    #query = "What is your analysis of Microsoft, Apple, NTAP, and Bank of America?"
    #query = "How do Microsoft, Nvidia, Advanced Micro Devices, ARM Holdings, and Campbell Soup compare?"
    #query = "Give me the stock symbols for Microsoft, Nvidia, Advanced Micro Devices, ARM Holdings, and Campbell Soup and how do these companies compare?"
    query = "What are stock symbols for Microsoft, NVDA, Advanced Micro Devices, ARM Holdings, and Campbell Soup and why and why should I invest in them?"
    print(query)    # This will print the query

    symbols = parse_query(query)
    print(symbols)  # This will print the list of stock symbols extracted from the query


