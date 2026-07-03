"""
MyAgent Registry

Registers built-in tools and plugin tools.
"""

from core.plugin_loader import load_plugins

# Filesystem tools
from core.tools import (
    create_folder,
    create_file,
    read_file,
    write_file,
    append_file,
    delete_file,
    copy_file,
    list_files,
    run_command,
)

# Project Builder
from core.project_builder import build_website

# Memory tools
from core.memory_tools import (
    remember,
    recall,
    forget,
    show_memory,
)

# --------------------------
# Built-in tools
# --------------------------

TOOLS = {
    # Filesystem
    "create_folder": create_folder,
    "create_file": create_file,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,
    "delete_file": delete_file,
    "copy_file": copy_file,
    "list_files": list_files,
    "run_command": run_command,

    # Website
    "build_website": build_website,

    # Memory
    "remember": remember,
    "recall": recall,
    "forget": forget,
    "show_memory": show_memory,
}

# --------------------------
# Load plugin tools
# --------------------------

TOOLS.update(load_plugins())


def execute_tool(task):
    tool_name = task.get("tool")
    args = task.get("args", [])

    if tool_name not in TOOLS:
        return f"Unknown tool: {tool_name}"

    try:
        return TOOLS[tool_name](*args)

    except Exception as e:
        return f"Tool Error: {e}"


def list_available_tools():
    return sorted(TOOLS.keys())
