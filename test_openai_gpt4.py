#------------------------------------------------------------
# test_openai_gpt4.py
# Purpose: Use this script to test that the environment 
# is connecting to OpenAI and an API is successfully invoked
#------------------------------------------------------------
print("Running openai-test-gpt4.py")
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Translate the following English text to French: 'Hello, world!'"}
  ]
)

print(completion.choices[0].message)
