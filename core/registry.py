from core.tools import (
    create_folder,
    read_file,
    list_files,
)

from core.project_builder import build_website

from core.memory_tools import (
    remember,
    recall,
    forget,
    show_memory,
)

TOOLS = {
    "create_folder": create_folder,
    "read_file": read_file,
    "list_files": list_files,
    "build_website": build_website,

    # Memory Tools
    "remember": remember,
    "recall": recall,
    "forget": forget,
    "show_memory": show_memory,
}


def execute_tool(task):
    tool = task.get("tool")
    args = task.get("args", [])

    if tool not in TOOLS:
        return f"Unknown tool: {tool}"

    try:
        return TOOLS[tool](*args)
    except Exception as e:
        return f"Tool Error: {e}"
