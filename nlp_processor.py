#------------------------------------------------------------
# nlp_processor.py
# Purpose:  The primary purpose of this script is to interpret 
#           user queries, extract relevant financial terms and 
#           concepts, and prepare them for processing to 
#           retrieve or calculate the requested financial data.
#------------------------------------------------------------
from openai import OpenAI

#------------------------------------------------------------
#
#
#------------------------------------------------------------
def process_query(user_query, structured_data):
    """
    Processes the user's financial query using OpenAI's API.

    :param user_query: The user's query as a string.
    :param structured_data: The structured data related to the financial query.
    :return: The processed response from OpenAI.
    """
    # Initialize the OpenAI client
    client = OpenAI()
    
    print("Running process_query()")
    print(user_query)
    print(structured_data)

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
        f"Let's talk about {company_name}, a company I've been looking into based on data from Alpha Vantage (https://www.alphavantage.co/). They have a Price-to-Earnings ratio of {pe_ratio}, which caught my eye. Their Profit Margin stands at {profit_margin}, and the Market Capitalization is currently {market_cap}. Interestingly, analysts have set a target price of {target_price}, while the Earnings per Share is {earnings_per_share} and EBITDA is {ebitda}. "
        + f"Digging deeper, I found that {company_name}'s Operating Margin TTM is {operating_margin_ttm}, with a Return on Equity TTM of {return_on_equity_ttm}. Their Beta value is {beta}, suggesting {beta_description} investment. The Book Value is noted as {book_value}, and their EV to EBITDA ratio is {ev_to_ebitda}, alongside a Gross Profit TTM of {gross_profit_ttm}. "
        + "Given these insights, I'm curious about your take on their financial health. Are there particular areas where you think the company could improve or aspects that signal strength?"
    )

    print(f"\nEnriched User Query:\n{detailed_description} ")

    # Here, adapt the messages to fit the context of your application.
    # For a financial query, you might want to include the structured_data in some way,
    # or just pass the query directly if the structured_data isn't needed here.
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that provides financial analysis."},
            {"role": "user", "content": detailed_description}
        ]
    )

    # Assuming the response structure matches your test case,
    # adjust if the actual response format differs.
    try:
        response = completion.choices[0].message  # Adjust based on actual response structure
    except IndexError:
        response = "An error occurred processing the query."

    webfile_write("archive.html", detailed_description, response)

    return response

#------------------------------------------------------------
#
#
#------------------------------------------------------------
def webfile_write(filename, question, answer):
    """Writes the question and answer into an HTML file with proper paragraph formatting."""
    # Ensure we are working with the string content of the answer
    answer_text = answer.content if hasattr(answer, 'content') else str(answer)
    
    # Split the answer_text into paragraphs on double newline characters
    paragraphs = answer_text.split('\n\n')
    
    # Wrap each paragraph with <p> tags
    formatted_answer = ''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs if paragraph.strip())

    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q&A Archive</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        .question, .answer {{ margin-bottom: 20px; }}
        .question h2, .answer h2 {{ margin-bottom: 10px; }}
    </style>
</head>
<body>
    <div class="question">
        <h2>Question:</h2>
        <p>{question}</p>
    </div>
    <div class="answer">
        <h2>Answer:</h2>
        {formatted_answer}
    </div>
</body>
</html>"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_template)





        

