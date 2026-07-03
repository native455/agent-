"""
MyAgent Registry

Version: 12.1.0
"""

from core.plugin_loader import load_plugins

# Built-in tools
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

# Memory tools
from core.memory_tools import (
    remember,
    recall,
    forget,
    show_memory,
)

TOOLS = {
    # Core tools
    "list_files": list_files,
    "create_folder": create_folder,
    "create_file": create_file,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,
    "delete_file": delete_file,
    "copy_file": copy_file,
    "run_command": run_command,

    # Memory tools
    "remember": remember,
    "recall": recall,
    "forget": forget,
    "show_memory": show_memory,
}

# Load plugins and merge them
TOOLS.update(load_plugins())


def execute_tool(task):

    tool_name = task.get("tool")
    args = task.get("args", [])

    if tool_name not in TOOLS:
        return {
            "success": False,
            "data": None,
            "error": f"Unknown tool: {tool_name}",
            "metadata": {
                "tool": tool_name
            }
        }

    try:

        result = TOOLS[tool_name](*args)

        # Already using Tool Result API
        if isinstance(result, dict) and "success" in result:
            return result

        # Legacy compatibility
        return {
            "success": True,
            "data": result,
            "error": None,
            "metadata": {
                "tool": tool_name,
                "legacy": True
            }
        }

    except Exception as e:

        return {
            "success": False,
            "data": None,
            "error": str(e),
            "metadata": {
                "tool": tool_name
            }
        }


def list_available_tools():
    return sorted(TOOLS.keys())
