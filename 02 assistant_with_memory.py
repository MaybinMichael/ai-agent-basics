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

messages = [
    {
                "role": "system",
                "content": f"You are a teacher. Respond to all the queries politely. Encourage the user."
            }
]

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "quit":
        print("\nAI: Goodbye, have a great day!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send a query to the FM 
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages=messages
    )

    # Display response
    ai_reply = response.choices[0].message.content
    print(f"AI: {ai_reply}")
    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )
    # print(response)
