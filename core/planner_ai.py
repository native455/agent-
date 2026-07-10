"""
Planner AI

Version: 13.2.0
"""

from core.ai import _request


SYSTEM_PROMPT = """
You are MyAgent's planning engine.

Return ONLY valid JSON.

Never explain.
Never reason.
Never use markdown.
Never wrap JSON in code fences.

If no tool is required return:

[]
"""


def ask_planner(messages):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ] + messages

    return _request(
        messages,
        temperature=0,
    )
