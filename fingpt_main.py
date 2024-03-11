#------------------------------------------------------------
# fingpt_main.py
# Purpose: 
#
#
#------------------------------------------------------------
import os
os.system('cls' if os.name == 'nt' else 'clear')
from stockSymbols import stock_symbols
#from stockMetrics import stock_metrics
#import utils
from utils import print_dict
from utils import get_mock_metrics
from nlpAnalyze import process_query
from stock_metrics_yfin import get_yf_stock_metrics
import pprint

print("Running fin_gpt_main.py")

def main():

	user_query = "What are stock symbols for Microsoft, NVDA, Advanced Micro Devices, ARM Holdings, Campbell Soup and why should I invest in them?"

	user_query = "What are stock symbols for Costco Wholesale, Kroger Co, Home Depot, Walmart and why should I invest in them?"

	user_query = "What are stock symbols for Costco Wholesale, Kroger Co and why should I invest in them? please respond with your finding that compare these companies in order of best to worst in terms of investment potential"

	#-----------------------------------------------------------
	# Get stock symbols for companies named in the user query
	# and get metrics for all named companies
	#-----------------------------------------------------------
	entity_symbols = stock_symbols(user_query)
	metric_data = get_yf_stock_metrics(entity_symbols) 

	print("\nMetric Data:")
	#print_dict(metric_data)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(metric_data)

	#-----------------------------------------------------------
	# Get final NLP text from GPT4
	#-----------------------------------------------------------
	process_query(user_query, metric_data)

if __name__ == "__main__":
	main()

