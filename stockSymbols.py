#------------------------------------------------------------
# stockSymbols.py
# Purpose: 
# Input data is a string containg a mix of stock symbols and
# company names such as: "Give me the stock symbols for Urban 
# Outfitters, GPS, American Eagle Outfitters and how do these
# companies compare?"
#------------------------------------------------------------
import re
from openai import OpenAI
from utils import webfile_write

def stock_symbols(user_query):
	# Extract names and symbols from the subjectNames section
	# of the user query. Then convert company names to 
	# stock symbols

	#------------------------------------------------------
	# Extract company names and stock symbols from the  
	# user query
	#------------------------------------------------------
	print(f"\nUser Query: {user_query}")
	pattern = re.compile(r'for(.*?)and (?:how|why)')
	matches = pattern.search(user_query)
	if matches:
		# Extract the matched group, strip leading/trailing spaces, and split by commas
		subject_names = matches.group(1).strip().split(',')
		# Clean whitespace around the names
		subject_names = [name.strip() for name in subject_names]
		#return subject_names
		print(f"\nsubject_names: {subject_names}")
	else:
		# If no matches are found, return an empty list
		print(f"\nsubject_names: NONE FOUND")
		#return []
	symbols = []

	#------------------------------------------------------
	# Call GPT4 to convert company names to stock symbols
	# leaving stock symbols unchanged
	#------------------------------------------------------
	detailed_description = (
        f"Give me stock symbols for the following mix of company names and "
        + f"stock symbols:  {subject_names}. "
    )

	print(f"\nsubject_names: {detailed_description}")

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
	print(f"\nGPT4 Response {response}")

	webfile_write('../archive.html', detailed_description, response)

	#------------------------------------------------------
	# Convert symbols from GPT4 response to a dictionary 
	# variable
	#------------------------------------------------------
	# Define a regular expression pattern to match "Company Name: Symbol"
	# This pattern assumes the symbol is represented by uppercase letters, digits, or periods

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


	print(f"\nSymbols Dictionary {symbols_dict}")

	# for name in company_names:
	#     symbol = ...  # Convert name to symbol
	#     symbols.append(symbol)
	return symbols_dict
