"""
MyAgent Registry

Registers built-in tools and plugin tools.
"""

from core.plugin_loader import load_plugins

# Load all plugin tools
TOOLS = load_plugins()


def execute_tool(task):
    """
    Execute a tool request.

    Expected format:
    {
        "tool": "tool_name",
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
    """Return all available tool names."""
    return sorted(TOOLS.keys())
