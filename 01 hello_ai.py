from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from .env
load_dotenv()

#Create a client that communicate with FM provider
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

# Send a query to the FM 
response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages=[
        {
            "role": "user",
            "content": "What is artificial intelligence?"
        }
    ]
)

#Display response
print(response.choices[0].message.content)
