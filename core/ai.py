"""
MyAgent AI Client

Version: 13.2.0
"""

import requests

from config import (
    API_KEY,
    API_URL,
    MODEL,
)


def _request(messages, model=None, temperature=0):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "MyAgent",
    }

    payload = {
        "model": model or MODEL,
        "messages": messages,
        "temperature": temperature,
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]


# Backward compatibility
def ask_ai(messages):
    return _request(messages)
