#------------------------------------------------------------
# test_openai_v5.py
# Purpose: Use this script to test that the environment 
# is connecting to OpenAI and an API is successfully invoked
#------------------------------------------------------------
print("Running test_openai_v5.py")
import openai
import os

# Set the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Translate the following English text to French: 'Hello, world!'"}
  ]
)

print(completion.choices[0].message['content'])
