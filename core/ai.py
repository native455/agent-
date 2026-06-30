import requests
from config import API_KEY, API_URL, MODEL

def ask_ai(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "MyAgent"
    }

    data = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=data,
        timeout=60
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
