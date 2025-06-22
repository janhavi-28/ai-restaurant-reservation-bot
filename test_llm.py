import os
from dotenv import load_dotenv
import requests

load_dotenv()  # <-- This loads your .env file

api_key = os.getenv("TOGETHER_API_KEY")
print("Using key:", api_key)

res = requests.post(
    "https://api.together.xyz/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [{"role": "user", "content": "Hello"}],
        "temperature": 0.7,
        "max_tokens": 10
    }
)

print(res.status_code)
print(res.text)
