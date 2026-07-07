"""
MyAgent Unified Tool Registry

Version: 13.0.1
"""

from core.plugin_loader import load_plugins

# Built-in tools
from core.memory_tools import (
    remember,
    recall,
    forget,
    show_memory,
)

from core.tools import (
    list_files,
    create_folder,
    create_file,
    read_file,
    write_file,
    append_file,
    delete_file,
    copy_file,
    run_command,
)

from core.project_tools import (
    create_project,
    open_project,
    close_project,
    list_projects,
    project_status,
    add_task,
    show_tasks,
    complete_task,
    add_note,
    show_notes,
)

from core.system_check import system_check

TOOLS = {

    # Memory
    "remember": remember,
    "recall": recall,
    "forget": forget,
    "show_memory": show_memory,

    # Files
    "list_files": list_files,
    "create_folder": create_folder,
    "create_file": create_file,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,
    "delete_file": delete_file,
    "copy_file": copy_file,
    "run_command": run_command,

    # Projects
    "create_project": create_project,
    "open_project": open_project,
    "close_project": close_project,
    "list_projects": list_projects,
    "project_status": project_status,
    "add_task": add_task,
    "show_tasks": show_tasks,
    "complete_task": complete_task,
    "add_note": add_note,
    "show_notes": show_notes,

    # System
    "system_check": system_check,
}

# Merge plugin tools
TOOLS.update(load_plugins())


def execute_tool(task):
    """
    Execute a tool request.

    Expected format:
    {
        "tool": "...",
        "args": [...]
    }
    """

    tool_name = task.get("tool")
    args = task.get("args", [])

    if tool_name not in TOOLS:
        return f"Unknown tool: {tool_name}"

    try:
        return TOOLS[tool_name](*args)
    except Exception as e:
        return f"Tool Error: {e}"


def list_available_tools():
    """
    Return every executable tool.
    """
    return sorted(TOOLS.keys())
