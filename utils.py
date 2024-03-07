#------------------------------------------------------------
# utils.py  
# Purpose: 
#------------------------------------------------------------
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




