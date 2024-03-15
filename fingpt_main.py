#------------------------------------------------------------
# fingpt_main.py
# Purpose: 
#
#------------------------------------------------------------
import os
#os.system('cls' if os.name == 'nt' else 'clear')
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

	user_query = "What are stock symbols for Costco Wholesale, Kroger Co, Home Depot, Walmart and why should I invest in them?"

	user_query = "What are stock symbols for Microsoft, NVDA, Advanced Micro Devices, ARM Holdings, Campbell Soup and why should I invest in them?"

	user_query = "What are stock symbols for Costco Wholesale, Kroger Co and why should I invest in them? please respond with your finding that compare these companies in order of best to worst in terms of investment potential"

	user_query = "Based on the following data for Microsoft, NVDA, Intel which stock may be the better investment?"

	user_query = "What are stock symbols for Microsoft, NVDA, Intel and why should I invest in them?"

	user_query = "What are stock symbols for #list Costco Wholesale, Kroger Co #list and why should I invest in them? please respond with your finding that compare these companies in order of best to worst in terms of investment potential"

	user_query = "What are stock symbols for #list Microsoft, NVDA, Intel #list and which stock may be the better investment?"

	user_query = "What are stock symbols for #listProcter & Gamble Co., Coca-Cola, Pepsi, Nike Inc, Colgate-Palmolive#list and why should I avoid investing in them?"

	user_query = "What are stock symbols for #list Microsoft, Apple #list and which stock may be the better investment?"

	user_query = "What are stock symbols for #list Northrop Grumman Corp, General Dynamics Corp, Boeing Co #list and which stock may be the better investment?"

	#-----------------------------------------------------------
	# Get stock symbols for companies named in the user query
	# and get metrics for all named companies
	#-----------------------------------------------------------
	entity_symbols = stock_symbols(user_query)
	metric_data = get_yf_stock_metrics(entity_symbols) 

	print("\nmetric_data:\n")
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(metric_data)

	#-----------------------------------------------------------
	# Get final NLP text from GPT4
	#-----------------------------------------------------------
	process_query(user_query, metric_data)

def process_user_query(user_query):

	try:
		# Your existing logic to process the query
		entity_symbols = stock_symbols(user_query)
		metric_data = get_yf_stock_metrics(entity_symbols)
		# Assuming process_query returns the analysis result as a string
		analysis_result = process_query(user_query, metric_data)

		# Make sure analysis_result is a string
		if analysis_result is None:
			return "No analysis result was returned."
		else:
			return analysis_result

	except Exception as e:
		# Catch any exceptions that occur and return them as a string
		return f"An error occurred: {e}"

if __name__ == "__main__":
	main()

