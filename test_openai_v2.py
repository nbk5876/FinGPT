# test_openai_v2.py
import os
from openai import OpenAI

print("####################################")
print("Running: test_openai_v2.py")

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()
print("KEY", api_key)

# Initialize the OpenAI client
client = OpenAI()

try:
    # Create a chat completion request
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate the following English text to French:"},
            {"role": "user", "content": "Hello, world!"}
        ]
    )

    # Print the completion result
    print(completion.choices[0].message['content'])
except Exception as e:
    print(f"An error occurred: {e}")
