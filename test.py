import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def ask(msg):
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": msg,
            },
        ]
    )
    print(chat_response.choices[0].message.content)

question = ""
while question != "1":
    ask(input("une question : "))