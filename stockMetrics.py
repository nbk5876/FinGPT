#------------------------------------------------------------
# stockMetrics.py
# Purpose: 
#
#------------------------------------------------------------
import requests
import os

#------------------------------------------------------------
# stock_metrics(symbols_dict, api_key)
# Purpose: Loop to get metrics for one or more stock symbols
#------------------------------------------------------------
def stock_metrics(symbols_dict):
    print(f"\nIn stock_metrics() with {symbols_dict}")
    metrics_dict = {}
    api_key = os.getenv('ALPHAVANTAGE_API_KEY')

    #symbols_dict = {'Microsoft': 'MSFT', 'NVIDIA': 'NVDA'}

    for company_name, symbol in symbols_dict.items():
        overview_data = get_stock_overview(symbol, api_key)
        if overview_data:
            metrics_dict[company_name] = overview_data
    return metrics_dict

#------------------------------------------------------------
# get_stock_overview(symbol, api_key)
# Purpose: Get metrics for 1 stock symbol
# https://www.alphavantage.co/documentation/#company-overview
#------------------------------------------------------------
def get_stock_overview(symbol, api_key):
    print(f"\nIn get_stock_overview() with {symbol}")
    api_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching overview for symbol {symbol}: {response.status_code}")
        return None

# Example usage:
# api_key = 'YOUR_ALPHAVANTAGE_API_KEY'
# symbols_dict = {'Microsoft': 'MSFT', 'NVIDIA': 'NVDA', ...}
# metrics_data = stock_metrics(symbols_dict, api_key)

if __name__ == "__main__":
	symbols_dict = {'Microsoft': 'MSFT', 'NVIDIA': 'NVDA'}
	metric_data = stock_metrics(symbols_dict)

	# Print the metrics data
	print("\nMetric Data:")
	for company, metrics in metric_data.items():
		print(f"\n{company}:")
		for key, value in metrics.items():
			print(f"{key}: {value}")