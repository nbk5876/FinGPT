#------------------------------------------------------------
# utils.py  
# Purpose: Contains utility functions
#------------------------------------------------------------

#------------------------------------------------------------
# get_mock_metrics()
# Purpose: Create mocked up data simulating the return from
#    alphavantage
#------------------------------------------------------------
def get_mock_metrics():
    mock_metric_data = {
        'overview': {
            'Costco Wholesale': {
                'Symbol': 'COST',
                'AssetType': 'Common Stock',
                'Name': 'Costco Wholesale Corp',
                'Description': 'Costco Wholesale Corporation is an American multinational corporation which operates a chain of membership-only big-box retail stores.',
                'Exchange': 'NASDAQ',
                'Currency': 'USD',
                'Country': 'USA',
                'Sector': 'TRADE & SERVICES',
                'MarketCapitalization': '321821409000',
                'EBITDA': '6251000000',
                'PERatio': '49.49',
                'EPS': '14.66',
                'Beta': '.87',
            },
            'Kroger Co': {
                'Symbol': 'KR',
                'AssetType': 'Common Stock',
                'Name': 'Kroger Company',
                'Description': 'The Kroger Company, or simply Kroger, is an American retail company founded by Bernard Kroger in 1883 in Cincinnati, Ohio.',
                'Exchange': 'NYSE',
                'Currency': 'USD',
                'Country': 'USA',
                'Sector': 'TRADE & SERVICES',
                'MarketCapitalization': '40298402000',
                'EBITDA': '6251000000',
                'PERatio': '21.78',
                'EPS': '2.57',
                'Beta': '1.4',
            },
            # ... additional companies ...
        },
        'currentPrice': {
            'COST': '500.00',  # Mock current price for Costco
            'KR': '42.00',    # Mock current price for Kroger
            # ... additional prices ...
        }
    }
    return mock_metric_data

def log_error(message):
    """Log an error message to the console."""
    print(f"ERROR: {message}")

def print_search_results(data):
    """
    Print search results in a human-readable format.

    Parameters:
    - data (dict): A dictionary containing a list of matches under the key 'bestMatches'.

    Each match is expected to be a dictionary containing details about a financial instrument.
    """
    print("Search Results:")
    for i, match in enumerate(data.get('bestMatches', []), start=1):
        print(f"\nResult {i}:")
        print(f"Symbol: {match.get('1. symbol', 'N/A')}")
        print(f"Name: {match.get('2. name', 'N/A')}")
        print(f"Type: {match.get('3. type', 'N/A')}")
        print(f"Region: {match.get('4. region', 'N/A')}")
        print(f"Market Hours: {match.get('5. marketOpen', 'N/A')} to {match.get('6. marketClose', 'N/A')} ({match.get('7. timezone', 'N/A')})")
        print(f"Currency: {match.get('8. currency', 'N/A')}")
        print(f"Match Score: {match.get('9. matchScore', 'N/A')}")

#------------------------------------------------------------
# webfile_write(filename, question, answer)
#
#------------------------------------------------------------
def webfile_write(filename, question, answer):
    #print(f"\nwriting webfile\n")
    # Ensure we are working with the string content of the answer
    answer_text = answer.content if hasattr(answer, 'content') else str(answer)
    
    # Replace newline characters with <br> tags for HTML line breaks
    formatted_answer = answer_text.replace('\n', '<br>')

    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q&A Archive</title>
    <style>
        body {{ font-family: Calibri, sans-serif; padding: 20px; }}
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


def print_dict(dictionary, indent=2):
    """
    Prints a dictionary to the console in a readable format.

    Parameters:
    - dictionary (dict): The dictionary to print.
    - indent (int): The number of spaces to use for indentation.
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            # If the value is another dictionary, recursively call this function
            print(f"{' ' * indent}{key}:")
            print_dict(value, indent=indent+2)
        else:
            # Otherwise, just print the key and value
            print(f"{' ' * indent}{key}: {value}")



