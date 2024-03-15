#------------------------------------------------------------
# test_openai_gpt4.py
# Purpose: Use this script to test that the environment 
# is connecting to OpenAI and an API is successfully invoked
# its a helloworld script
# Last good run date: 3/13/2024
# API Status Console: https://platform.openai.com/usage
#------------------------------------------------------------
print(f"=============================================\nRunning openai-test-gpt4.py using model gpt-4\n=============================================")
from openai import OpenAI
client = OpenAI()

userContent = "Translate the following English text to French: 'Hello, world!'"

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"{userContent}"}
  ]
)

print(f"\n{userContent}")
print(completion.choices[0].message)


