#------------------------------------------------------------
# nlpAnalyze.py
# Purpose: Send enriched user queries to GPT-4 to be 
# analyzed per the users direction
#
#------------------------------------------------------------
from openai import OpenAI
from utils import webfile_write

def process_query(user_query, structured_data):
    print(f"\nIn process_query with '{user_query}'':")
    print("Structured Data:")
    print("===================================")
    print(structured_data)
    print("===================================")

    # Initialize the OpenAI client
    client = OpenAI()

    # Initialize a list to hold individual company analysis strings
    company_analysis_list = []

    for ticker_symbol, metrics in structured_data.items():
        # Prepare the individual analysis string for each company
        analysis_str = (
            f"{ticker_symbol} - Market Cap: {metrics.get('marketCap', 'Data not available')}, "
            f"PE Ratio: {metrics.get('trailingPE', 'Data not available')}, "
            f"Beta: {metrics.get('beta', 'Data not available')}, "
            f"Current Price: {metrics.get('currentPrice', 'Data not available')}, "
            f"EBITDA: {metrics.get('ebitda', 'Data not available')}, "
            f"Gross Margins: {metrics.get('grossMargins', 'Data not available')}, "
            f"Book Value: {metrics.get('bookValue', 'Data not available')}, "
            f"Earnings Growth: {metrics.get('earningsGrowth', 'Data not available')}, "
            f"Revenue Growth: {metrics.get('revenueGrowth', 'Data not available')}, "
            f"Dividend Yield: {metrics.get('dividendYield', 'Data not available')}, "
            f"Return on Equity: {metrics.get('returnOnEquity', 'Data not available')}, "
            f"Forward PE: {metrics.get('forwardPE', 'Data not available')}, "
            f"Debt to Equity: {metrics.get('debtToEquity', 'Data not available')}, "
            f"52 Week Change: {metrics.get('52WeekChange', 'Data not available')}, "
            f"Average Volume: {metrics.get('averageVolume', 'Data not available')}."
        )
        company_analysis_list.append(analysis_str)

    # Join all individual company analysis strings into one big analysis query
    combined_analysis_query = "Comparative analysis: " + " ".join(company_analysis_list)

    print(f"\n----------------------------------------------------------\nCombined Analysis Query is: \n{combined_analysis_query}\n----------------------------------------------------------\n")

    # Send this combined analysis query to GPT-4 for further analysis
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that provides financial analysis."},
            {"role": "user", "content": combined_analysis_query}
        ]
    )

    try:
        response = completion.choices[0].message.content  # Adjust based on actual response structure
        print(f"\n-(AA)-----(AA)-----(AA)------(AA)-----\nGPT-4 Comparative Analysis: \n{response}")
        webfile_write('../archive.html', user_query + '\n\n<br><br>' + combined_analysis_query, response)
    except IndexError:
        print(f"An error occurred processing the combined query.\n")
