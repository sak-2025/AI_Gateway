import os

import openai
from dotenv import load_dotenv

load_dotenv()  # reads INTERN_KEY from the project's .env

client = openai.OpenAI(
    api_key=os.environ["INTERN_KEY"],
    base_url="http://localhost:4000",
    max_retries=0,  # no hidden retries: show the first rejection immediately
)

try:
    response = client.chat.completions.create(
        model="advanced-reasoning-model",
        messages=[
            {
                "role": "user",
                "content": "Draft a polite email requesting a meeting",
            }
        ],
    )
    print("ACCEPTED")
    print(response.choices[0].message.content)
except openai.APIStatusError as e:
    # Blocked by the gateway: show the real status code and message
    print("REJECTED")
    print("Status code:", e.status_code)
    print("Message:", e.message)
