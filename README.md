# README.md for FinGPT GitHub Repository

## FinGPT Prototype
FinGPT is a small Python application that provides financial analysis of stock market information by working together with ChatGPT. Users enter the symbol for an equity, e.g. MSFT, AAPL etc, and receives detailed insights, market analysis, historical performance, and predictive trends. The application is intended as a prototype to show how ChatGPT can be integrated with stock market data using application programing interfaces (APIs). 

![Example Image](https://nbk5876.github.io/FinGPT/image/FinGpt-Prototype-Concept-Diagram.png "FinGPT Overview Flow")

## Table of Contents
- Installation
- Usage
- Contributing
- License

## Installation
Before installation, ensure you have Python (version 3.8 or newer) installed on your system.

**Clone the Repository**

git clone https://github.com/nbk5876/FinGPT

cd GPTFin

**Setup a Virtual Environment**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install Dependancies**

pip install -r requirements.txt

This will install all necessary Python packages, including openai, which is required for interfacing with GPT-4. 

## Usage
To use FinGPT, run the main script from a command line prompt:

python fin_gpt_main.py

Upon launch, the application will prompt you to enter an equity symbol (e.g., AAPL for Apple Inc.). After submission, FinGPT processes your request and outputs a detailed financial analysis report, including:

Current stock price and volume
Latest news and analyst recommendations
Predictive trends and investment advice

## Contributing
Guidelines for contributing have not been set but are welcome.

## License
The license has not been set.


