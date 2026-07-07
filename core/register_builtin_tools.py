"""
Register Built-in Tool Metadata

MyAgent V13.0.0
"""

from core.tool_metadata import register_tool
from core.system_check import system_check

# Project tools
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


def register_builtin_tools():
    """
    Register metadata for all built-in tools.
    """

    # ==========================
    # Memory Tools
    # ==========================

    register_tool(
        "remember",
        "Store information in long-term memory.",
        ["key", "value"],
    )

    register_tool(
        "recall",
        "Retrieve information from memory.",
        ["key"],
    )

    register_tool(
        "forget",
        "Delete information from memory.",
        ["key"],
    )

    register_tool(
        "show_memory",
        "Display all stored memories.",
        [],
    )

    # ==========================
    # File Tools
    # ==========================

    register_tool(
        "list_files",
        "List files inside a directory.",
        [],
    )

    register_tool(
        "create_folder",
        "Create a new folder.",
        ["folder"],
    )

    register_tool(
        "create_file",
        "Create an empty file.",
        ["filename"],
    )

    register_tool(
        "read_file",
        "Read the contents of a file.",
        ["filename"],
    )

    register_tool(
        "write_file",
        "Write text into a file.",
        ["filename", "content"],
    )

    register_tool(
        "append_file",
        "Append text to a file.",
        ["filename", "content"],
    )

    register_tool(
        "delete_file",
        "Delete a file.",
        ["filename"],
    )

    register_tool(
        "copy_file",
        "Copy one file to another location.",
        ["source", "destination"],
    )

    register_tool(
        "run_command",
        "Execute a shell command.",
        ["command"],
    )

    # ==========================
    # Project Assistant Tools
    # ==========================

    register_tool(
        "create_project",
        "Create a new software project.",
        ["name"],
    )

    register_tool(
        "open_project",
        "Open an existing project.",
        ["name"],
    )

    register_tool(
        "close_project",
        "Close the active project.",
        [],
    )

    register_tool(
        "list_projects",
        "List every project.",
        [],
    )

    register_tool(
        "project_status",
        "Show information about the active project.",
        [],
    )

    register_tool(
        "add_task",
        "Add a task to the active project.",
        ["task"],
    )

    register_tool(
        "show_tasks",
        "Display every task in the active project.",
        [],
    )

    register_tool(
        "complete_task",
        "Mark a task as completed.",
        ["task_number"],
    )

    register_tool(
        "add_note",
        "Add a note to the active project.",
        ["note"],
    )

    register_tool(
        "show_notes",
        "Display notes from the active project.",
        [],
    )

    # ==========================
    # System Tools
    # ==========================

    register_tool(
        "system_check",
        "Check the health of the MyAgent installation.",
        [],
    )
