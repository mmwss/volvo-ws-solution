import requests
from assistant.const import API_KEY, PROJECT_ID

response = requests.post(
  "https://api.openai.com/v1/chat/completions",
  headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    "OpenAI-Project": PROJECT_ID,
  },
  json={
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }
)

print(f"""
Response:
{response.json()["choices"][0]["message"]["content"]}
""")
