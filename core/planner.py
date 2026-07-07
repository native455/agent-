"""
Dynamic Planner

MyAgent V12.3
"""

import json

from core.ai import ask_ai
from core.registry import list_available_tools


def build_prompt():
    """
    Build the planner prompt dynamically from all
    registered tools.
    """

    tools = list_available_tools()

    tool_list = "\n".join(f"- {tool}" for tool in tools)

    return f"""
You are MyAgent's autonomous planner.

Return ONLY valid JSON.

Available tools:

{tool_list}

Rules:

1. Return ONLY valid JSON.
2. Never include explanations.
3. If no tools are required, return [].
4. If one tool is needed, return a JSON array containing one object.
5. Every task MUST use this format:

[
    {{
        "tool": "tool_name",
        "args": []
    }}
]
"""


def plan_task(user):

    messages = [
        {
            "role": "system",
            "content": build_prompt()
        },
        {
            "role": "user",
            "content": user
        }
    ]

    reply = ask_ai(messages)

    print("\n========== PLANNER RAW RESPONSE ==========")
    print(reply)
    print("==========================================\n")

    try:

        data = json.loads(reply)

        # If AI returned a single object instead of a list
        if isinstance(data, dict):
            return [data]

        # If AI returned a proper list
        if isinstance(data, list):
            return data

        return []

    except Exception as e:

        print("Planner JSON Error:", e)

        return []
