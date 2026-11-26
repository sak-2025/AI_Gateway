import os

import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ["FRAUD_KEY"],
    base_url="http://localhost:4000",
    max_retries=0,
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
    # Blocked by the gateway
    print("REJECTED")
    print("Status code:", e.status_code)
    print("Message:", e.message)
