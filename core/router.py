import json
from core.ai import ask_ai

SYSTEM_PROMPT = """
You are the routing brain of MyAgent.

Return ONLY valid JSON.

Available tools:

create_folder(folder_name)
read_file(filename)
list_files()
build_website(project_name)

If the user wants to use one or more tools return:

[
  {
    "tool":"tool_name",
    "args":[]
  }
]

If no tool is needed return:

[]
"""

def decide(user):

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
