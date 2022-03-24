import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    start_sequence = "\nAI:"
    restart_sequence = input("\nHuman:")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"\nHuman: {restart_sequence}\nAI: {start_sequence}",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    print(response.choices[0].text)
