# first-req.py
import os
from openai import OpenAI

print("####################################")
print("Running: first_req.py")

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

# Explicitly set the API key for OpenAI
OpenAI.api_key = api_key

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)