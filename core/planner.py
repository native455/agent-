import json
from core.ai import ask_ai

SYSTEM_PROMPT = """
You are MyAgent's autonomous planner.

Return ONLY valid JSON.

Available tools:

create_folder(folder)

read_file(file)

list_files()

build_website(project)

remember(key,value)

recall(key)

forget(key)

show_memory()

Examples:

User:
Remember my name is Okechukwu

Return:

[
    {
        "tool":"remember",
        "args":["name","Okechukwu"]
    }
]

User:
What's my name?

Return:

[
    {
        "tool":"recall",
        "args":["name"]
    }
]

User:
Build a portfolio website

Return:

[
    {
        "tool":"create_folder",
        "args":["Portfolio"]
    },
    {
        "tool":"build_website",
        "args":["Portfolio"]
    }
]

If no tools are needed return:

[]
"""


def plan_task(user):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user
        }
    ]

    reply = ask_ai(messages)

    try:
        return json.loads(reply)

    except Exception:
        return []
