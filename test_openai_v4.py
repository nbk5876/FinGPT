#------------------------------------------------------------
# test_openai_v4.py
# Purpose: Use this script to test that the environment 
# is connecting to OpenAI and an API is successfully invoked
# Version Note: 

#------------------------------------------------------------
print("Running openai-test.py")
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Translate the following English text to French:"},
    {"role": "user", "content": "Hello, world!"}
  ]
)

print(completion.choices[0].message)