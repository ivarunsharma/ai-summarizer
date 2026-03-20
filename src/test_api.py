import os
import anthropic
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Say hello and tell me one fun fact about Python programming."}
    ]
)

print(response.content[0].text)