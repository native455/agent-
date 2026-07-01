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

from core.plugin_loader import load_plugins


TOOLS = {

    # ==========================
    # Built-in File Tools
    # ==========================
    "create_folder": create_folder,
    "read_file": read_file,
    "list_files": list_files,

    # ==========================
    # Project Builder
    # ==========================
    "build_website": build_website,

    # ==========================
    # Memory Tools
    # ==========================
    "remember": remember,
    "recall": recall,
    "forget": forget,
    "show_memory": show_memory,
}


# =====================================
# Load every plugin automatically
# =====================================
TOOLS.update(load_plugins())


def execute_tool(task):
    """
    Execute a task dictionary.

    Example:

    {
        "tool":"create_folder",
        "args":["Portfolio"]
    }
    """

    tool = task.get("tool")
    args = task.get("args", [])

    if tool not in TOOLS:
        return f"Unknown tool: {tool}"

    try:
        return TOOLS[tool](*args)

    except Exception as e:
        return f"Tool Error: {e}"
