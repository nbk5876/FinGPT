#------------------------------------------------------------
# stockSymbols.py
# Purpose: 
# Input data is a string containg a mix of stock symbols and
# company names such as: "Give me the stock symbols for Urban 
# Outfitters, GPS, American Eagle Outfitters and how do these
# companies compare?"
#------------------------------------------------------------
import re
import os
import pprint
from openai import OpenAI
from utils import webfile_write




#------------------------------------------------------
# stock_symbols(user_query)
# 
#------------------------------------------------------
def stock_symbols(user_query):
	print(f"\n=(A)==========(A)==========(A)=========(A)=========(A)====================\nRunning stock_symbols(user_query) with:\n{user_query}")
	subject_names = []

	pattern = re.compile(r'#list(.*?)#list', re.IGNORECASE | re.DOTALL)

	matches = pattern.findall(user_query)
	if matches:
		# Since findall returns a list of matches, we take the first match assuming there's only one relevant list
		subject_names_str = matches[0].strip()
		subject_names = [name.strip() for name in subject_names_str.split(',')]
		print(f"\n-(B)-------------------------------\nsubject_names: {subject_names}")
	else:
		print(f"\nsubject_names: NONE FOUND")

	#symbols = []

	#------------------------------------------------------
	# Call GPT4 to convert company names to stock symbols
	# leaving stock symbols unchanged
	#------------------------------------------------------
	#detailed_description = (
    #    f"Give me stock symbols for the following mix of company names and "
    #    + f"stock symbols:  {subject_names}. "
    #)


	detailed_description = (
		"List the stock symbols for the following companies in the format 'Company Name: Stock Symbol', "
		+ f"one per line: {', '.join(subject_names)}. Please be concise."
	)




	print(f"\n-(C)-------------------------------\ndetailed_description: {detailed_description}")

	client = OpenAI()
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
	
	print(f"\n-(D)-------------------------------\nGPT4 Response \n{response}\n")

	webfile_write('../archive.html', detailed_description, response)

	#------------------------------------------------------
	# Convert symbols from GPT4 response to a dictionary 
	# variable
	#------------------------------------------------------
	# Ensure we are working with the string content of the response
	response_content = response.content if hasattr(response, 'content') else str(response)

	#pattern = re.compile(r'(\w[\w\s]+?): (\w+|\w+\.\w+)')
	pattern = re.compile(r'([\w\s]+?): ([A-Z]+[A-Z0-9.]*)')

	# Search for all occurrences of the pattern
	matches = pattern.findall(response_content)

	# Convert matches to a dictionary
	#symbols_dict = {match[0].strip(): match[1].strip() for match in matches}

	# Convert matches to a dictionary, ignoring any entries that capture comments instead of symbols
	symbols_dict = {}
	for company, symbol in matches:
		# Check if the symbol is valid (not starting with "This" which is likely from a comment)
		if not symbol.startswith("This"):
			symbols_dict[company.strip()] = symbol.strip()

	print(f"-(E)-------------------------------\nSymbols Dictionary {symbols_dict}")

	# for name in company_names:
	#     symbol = ...  # Convert name to symbol
	#     symbols.append(symbol)
	return symbols_dict

if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	pp = pprint.PrettyPrinter(indent=4)
	print(f"Debugging stockSymbols.py")

	#testQry0 = "What are stock symbols for <CompanyOrStockSymbol1>, <CompanyOrStockSymbol2>, <CompanyOrStockSymbol3> and why should I invest in them?"
	#testQry1 = "What are stock symbols for Microsoft, NVDA, Intel and why should I invest in them?"
	#testQry2 = "What are stock symbols for Microsoft, NVDA, Intel and which stock may be the better investment?"
	#testQry3 = "Based on the following data for Microsoft, NVDA, Intel, which stock may be the better investment?"
	#testQry4 = "Microsoft, NVDA, Intel"
	#testQry5 = "Procter & Gamble Co., Coca-Cola, Pepsi, Nike Inc, Colgate-Palmolive"


	testQry6 = "What are stock symbols for #list Microsoft, NVDA, Intel #list and which stock may be the better investment?"
	testQry7 = "What are stock symbols for #listMicrosoft, NVDA, Intel #list and why should I invest in them?"
	testQry8 = "What are stock symbols for #listProcter & Gamble Co., Coca-Cola, Pepsi, Nike Inc, Colgate-Palmolive#list and why should I avoid investing in them?"
	testQry9 = "#listMicrosoft, NVDA, Intel #list"

	entity_symbols = stock_symbols(testQry6)
	pp.pprint(entity_symbols)

	entity_symbols = stock_symbols(testQry7)
	pp.pprint(entity_symbols)

	entity_symbols = stock_symbols(testQry8)
	pp.pprint(entity_symbols)

	entity_symbols = stock_symbols(testQry9)
	pp.pprint(entity_symbols)

