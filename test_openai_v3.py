#------------------------------------------------------------
# test_openai_v3.py
# Purpose: Use this script to test that the environment 
# is connecting to OpenAI and an API is successfully invoked
#------------------------------------------------------------
import os
import openai

print("####################################")
print("Running: test_openai_v3.py")

# Retrieve the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

try:
    # Create a chat completion request using the direct openai function call
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate the following English text to French:"},
            {"role": "user", "content": "Hello, world!"}
        ]
    )

    # Print the completion result
    print(completion['choices'][0]['message']['content'])
except Exception as e:
    print(f"An error occurred: {e}")
