#------------------------------------------------------------
# nlpAnalyze.py
# Purpose: Send enriched user queries to GPT-4 to be 
# analyzed per the users direction
#
#------------------------------------------------------------
from openai import OpenAI

#------------------------------------------------------------
# process_query(user_query, structured_data)
# Purpose: Send enriched user queries to GPT-4 to be 
# analyzed per the users direction
#------------------------------------------------------------
def process_queryZZ(user_query, structured_data):
    print(f"\nin process_query with {user_query}")
    print("Running process_query()")
    print(f"user_query: {user_query}")
    print(f"\nstructured_data: {structured_data}")

    # Initialize the OpenAI client
    client = OpenAI()

    for company_name, company_metrics in structured_data['overview'].items():
        # Directly access the company's data within the 'overview' dictionary
        symbol = company_metrics.get("Symbol", "Data not available")
        market_cap = company_metrics.get("MarketCapitalization", "Data not available")
        pe_ratio = company_metrics.get("PERatio", "Data not available")
        eps = company_metrics.get("EPS", "Data not available")
        beta = company_metrics.get("Beta", "Data not available")

        # Access the current price from the 'currentPrice' dictionary using the company name
        current_price = structured_data['currentPrice'].get(company_name, "Data not available")

        # Prepare your analysis query based on extracted data
        analysis_query = f"{company_name} ({symbol}) has a market capitalization of {market_cap}, a PE ratio of {pe_ratio}, EPS of {eps}, and a beta of {beta}. The current price is {current_price}."

        # Send this analysis query to GPT-4 for further analysis
        # Example GPT-4 call (adjust according to your implementation)
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that provides financial analysis."},
                {"role": "user", "content": analysis_query}
            ]
        )

        try:
            response = completion.choices[0].message.content  # Adjust based on actual response structure
            print(f"\nGPT-4 Analysis for {company_name}: {response}")
        except IndexError:
            print(f"An error occurred processing the query for {company_name}.")


        # Add additional processing as needed

def process_query(user_query, structured_data):
    print("\nin process_query with user_query:")
    print(user_query)
    print("Structured Data:")
    print(structured_data)

    # Initialize the OpenAI client
    client = OpenAI()

    for ticker_symbol, metrics in structured_data.items():
        # Prepare your analysis query based on extracted data
        current_price = metrics.get('currentPrice', "Data not available")
        market_cap = metrics.get('marketCap', "Data not available")
        pe_ratio = metrics.get('trailingPE', "Data not available")
        beta = metrics.get('beta', "Data not available")

        analysis_query = f"{ticker_symbol} has a market capitalization of {market_cap}, a PE ratio of {pe_ratio}, and a beta of {beta}. The current price is {current_price}."

        # Send this analysis query to GPT-4 for further analysis
        # Example call to GPT-4 (adjust according to your implementation)
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that provides financial analysis."},
                {"role": "user", "content": analysis_query}
            ]
        )

        try:
            response = completion.choices[0].message.content  # Adjust based on actual response structure
            print(f"\nGPT-4 Analysis for {ticker_symbol}: {response}")
        except IndexError:
            print(f"An error occurred processing the query for {ticker_symbol}.")






















"""
#------------------------------------------------------------
# process_query(user_query, structured_data)
# Purpose: Send enriched user queries to GPT-4 to be 
# analyzed per the users direction
#------------------------------------------------------------
def process_queryZZZ(user_query, structured_data):
	print(f"\nin process_query with {user_query}")

	# Initialize the OpenAI client
	client = OpenAI()

	print("Running process_query()")
	print(f"user_query: {user_query}")
	print(f"structured_data: {structured_data}")

	# Extract required information from structured_data
	company_name = structured_data["overview"].get("Name")
 
	# Extract required information from structured_data
	company_name = structured_data["overview"].get("Name")
	pe_ratio = structured_data["overview"].get("PERatio")
	market_cap = structured_data["overview"].get("MarketCapitalization")
	target_price = structured_data["overview"].get("AnalystTargetPrice")
	profit_margin = structured_data["overview"].get("ProfitMargin")
	ebitda = structured_data["overview"].get("EBITDA")
	operating_margin_ttm = structured_data["overview"].get("OperatingMarginTTM")
	return_on_equity_ttm = structured_data["overview"].get("ReturnOnEquityTTM")
	beta = structured_data["overview"].get("Beta")
	book_value = structured_data["overview"].get("BookValue")
	ev_to_ebitda = structured_data["overview"].get("EVToEBITDA")
	gross_profit_ttm = structured_data["overview"].get("GrossProfitTTM")
	earnings_per_share = structured_data["overview"].get("EPS")
	current_price = structured_data["currentPrice"]

	print(f"Price to Earnings ratio is {pe_ratio} for {structured_data.get('Name')}")

	# Pre-calculate the beta description to avoid complexity within the f-string
	beta_description = "a relatively stable" if float(beta) < 1 else "a potentially more volatile"
	detailed_description = (
		f"Let's talk about {company_name}, a company I've been looking into using data from Alpha Vantage (https://www.alphavantage.co/). They have a Price-to-Earnings ratio of {pe_ratio}, which caught my eye. Their Profit Margin stands at {profit_margin}, and the Market Capitalization is currently {market_cap}. Interestingly, analysts have set a target price of {target_price}, while the Earnings per Share is {earnings_per_share} and EBITDA is {ebitda}. "
		+ f"Digging deeper, I found that {company_name}'s Operating Margin TTM is {operating_margin_ttm}, with a Return on Equity TTM of {return_on_equity_ttm}. Their Beta value is {beta}, suggesting {beta_description} investment. The Book Value is noted as {book_value}, and their EV to EBITDA ratio is {ev_to_ebitda}, alongside a Gross Profit TTM of {gross_profit_ttm}. "
		+ "Given these insights, I'm curious about your take on their financial health. Are there particular areas where you think the company could improve or aspects that signal strength?"
	)

	print(f"\nEnriched User Query:\n{detailed_description} ")

"""