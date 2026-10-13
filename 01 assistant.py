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


print("="*40)
print("My AI Assistant")
print("="*40)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "quit":
        print("\nAI: Goodbye, have a great day!")
        break

    # Send a query to the FM 
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    # Display response
    print(response.choices[0].message.content)
    print(response)
