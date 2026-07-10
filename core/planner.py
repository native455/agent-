"""
Dynamic Planner

MyAgent V13.4.0
"""

import json

from core.planner_ai import ask_planner
from core.registry import list_available_tools


def build_prompt():

    tools = list_available_tools()

    tool_list = "\n".join(f"- {tool}" for tool in tools)

    return f"""
You are MyAgent's planning engine.

Return ONLY valid JSON.

Available tools:

{tool_list}

Rules:

1. Return ONLY JSON.
2. Never explain.
3. Never think aloud.
4. Never use markdown.
5. Never wrap JSON in code blocks.
6. If no tool is required return [].

Coding Rules:

- If the user asks to create a Flask project, use create_code_project.
- If the user asks to create a Python project, use create_code_project.
- If the user asks to build a website, use build_website.
- If the user asks to inspect a project, use scan_project.
- If the user asks to read source code, use read_code_file.
- If the user asks to modify source code, use write_code_file.

Terminal Rules:

- If the user wants to run a safe shell command, use terminal_command.
- If the user asks for git status, use git_status.
- If the user asks for git branches, use git_branch.
- If the user asks for git history, use git_log.
- If the user wants to commit changes, use git_commit.
- If the user wants to install a Python package, use pip_install.
- If the user wants to uninstall a Python package, use pip_uninstall.
- If the user wants to run npm install, use npm_install.
- If the user wants to install an npm package, use npm_package.

Intelligence Rules:

- If the user asks to analyze a Python file, use analyze_code_file.
- If the user asks to summarize or inspect a project, use project_summary.
- If the user asks to index a project, use index_code_project.
- If the user asks about imports or module relationships, use scan_dependencies.
Example:

[
    {{
        "tool": "read_file",
        "args": ["README.md"]
    }}
]
"""


def _extract_json(text):

    text = text.strip()

    if text.startswith("["):
        return text

    start = text.find("[")
    end = text.rfind("]")

    if start != -1 and end != -1:
        return text[start:end + 1]

    return "[]"


def plan_task(user):

    messages = [
        {
            "role": "system",
            "content": build_prompt(),
        },
        {
            "role": "user",
            "content": user,
        },
    ]

    reply = ask_planner(messages)

    print("\n========== PLANNER RAW RESPONSE ==========")
    print(reply)
    print("==========================================\n")

    reply = _extract_json(reply)

    try:

        data = json.loads(reply)

        if isinstance(data, dict):
            return [data]

        if isinstance(data, list):
            return data

        return []

    except Exception as e:

        print("Planner JSON Error:", e)

        return []
