"""
Register Built-in Tool Metadata

MyAgent

Version: 13.3.2
"""

from core.tool_metadata import register_tool

# Import built-in modules
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

# Context tools
from core.context_tools import (
    show_context,
    set_project_context,
    set_folder_context,
    set_file_context,
    set_mode,
    clear_context,
)


def register_builtin_tools():
    """
    Register metadata for every built-in tool.
    """

    # ==========================================
    # Memory
    # ==========================================

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
        "Display every stored memory.",
        [],
    )

    # ==========================================
    # File Tools
    # ==========================================

    register_tool(
        "list_files",
        "List files in a directory.",
        [],
    )

    register_tool(
        "create_folder",
        "Create a folder.",
        ["folder"],
    )

    register_tool(
        "create_file",
        "Create a file.",
        ["filename"],
    )

    register_tool(
        "read_file",
        "Read a file.",
        ["filename"],
    )

    register_tool(
        "write_file",
        "Write a file.",
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
        "Copy a file.",
        ["source", "destination"],
    )

    register_tool(
        "run_command",
        "Execute a shell command.",
        ["command"],
    )

    # ==========================================
    # Project Assistant
    # ==========================================

    register_tool(
        "create_project",
        "Create a software project.",
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
        "List all projects.",
        [],
    )

    register_tool(
        "project_status",
        "Display active project status.",
        [],
    )

    register_tool(
        "add_task",
        "Add a task.",
        ["task"],
    )

    register_tool(
        "show_tasks",
        "Show all project tasks.",
        [],
    )

    register_tool(
        "complete_task",
        "Complete a task.",
        ["task_number"],
    )

    register_tool(
        "add_note",
        "Add a project note.",
        ["note"],
    )

    register_tool(
        "show_notes",
        "Show project notes.",
        [],
    )

    # ==========================================
    # Context Engine
    # ==========================================

    register_tool(
        "show_context",
        "Show the current context.",
        [],
    )

    register_tool(
        "set_project_context",
        "Set the active project context.",
        ["project"],
    )

    register_tool(
        "set_folder_context",
        "Set the active folder context.",
        ["folder"],
    )

    register_tool(
        "set_file_context",
        "Set the active file context.",
        ["file"],
    )

    register_tool(
        "set_mode",
        "Change the current operating mode.",
        ["mode"],
    )

    register_tool(
        "clear_context",
        "Clear the current context.",
        [],
    )

    # ==========================================
    # Coding Engine
    # ==========================================

    register_tool(
        "create_code_project",
        "Create a new project from a template.",
        ["project_type", "project_name"],
    )

    register_tool(
        "build_website",
        "Generate a complete HTML/CSS/JS website.",
        ["project_name"],
    )

    register_tool(
        "scan_project",
        "Scan an existing project.",
        ["project_path"],
    )

    register_tool(
        "read_code_file",
        "Read a source code file.",
        ["filename"],
    )

    register_tool(
        "write_code_file",
        "Overwrite a source code file.",
        ["filename", "content"],
    )

    # ==========================================
    # Terminal Engine
    # ==========================================

    register_tool(
        "terminal_command",
        "Execute a safe terminal command.",
        ["command"],
    )

    register_tool(
        "git_status",
        "Show git repository status.",
        [],
    )

    register_tool(
        "git_branch",
        "List git branches.",
        [],
    )

    register_tool(
        "git_log",
        "Show git commit history.",
        [],
    )

    register_tool(
        "git_add",
        "Stage all modified files.",
        [],
    )

    register_tool(
        "git_commit",
        "Commit staged files.",
        ["message"],
    )

    register_tool(
        "pip_install",
        "Install a Python package.",
        ["package"],
    )

    register_tool(
        "pip_uninstall",
        "Uninstall a Python package.",
        ["package"],
    )

    register_tool(
        "npm_install",
        "Run npm install.",
        [],
    )

    register_tool(
        "npm_package",
        "Install an npm package.",
        ["package"],
    )    # ==========================================
    # System
    # ==========================================
    # Intelligence Engine
    # ==========================================

    register_tool(
        "analyze_code_file",
        "Analyze a Python source file.",
        ["filename"],
    )

    register_tool(
        "index_code_project",
        "Index all Python symbols in a project.",
        ["project"],
    )

    register_tool(
        "scan_dependencies",
        "Scan project dependencies.",
        ["project"],
    )

    register_tool(
        "project_summary",
        "Generate a project summary.",
        ["project"],
    )    # ==========================================

    register_tool(
        "system_check",
        "Check the health of MyAgent.",
        [],
    )

