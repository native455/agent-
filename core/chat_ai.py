"""
Chat AI

Version: 13.2.0
"""

from core.ai import _request


SYSTEM_PROMPT = """
You are MyAgent.

You are a helpful AI assistant running inside Termux.

Be concise, accurate and helpful.

Never expose internal planning or reasoning.
"""


def ask_chat(messages):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ] + messages

    return _request(
        messages,
        temperature=0.7,
    )
