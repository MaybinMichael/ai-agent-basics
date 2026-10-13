from datetime import datetime

def get_current_time():
    """return current date and time"""
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


import random
def roll_dice():
    """return a random number between 1 and 6"""
    return random.randint(1,6)


import secrets
import string

def generate_password(length=12):
    """Generate a secure password"""
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password




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
                "content": f"You are a assistant. Respond to all the queries politely."
            }
]

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "quit":
        print("\nAI: Goodbye, have a great day!")
        break

    if "time" in user_input.lower():
        print("\nAI: ", get_current_time())
        continue
    elif "dice" in user_input.lower():
        print("\nAI: ", roll_dice())
        continue
    elif "password" in user_input.lower():
        print("\nAI: ", generate_password())
        continue

    
    
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
