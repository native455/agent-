"""
Coder AI

Version: 13.2.1
"""

from core.ai import _request


SYSTEM_PROMPT = """
You are MyAgent's coding engine.

You specialize in:

- Python
- JavaScript
- HTML
- CSS
- React
- Flask
- FastAPI
- SQL
- Shell scripting

Always generate clean, production-ready code.

Never expose internal reasoning.

Return only the requested code or explanation.
"""


def ask_coder(messages):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ] + messages

    return _request(
        messages,
        temperature=0.2,
    )
