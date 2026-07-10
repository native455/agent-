
"""
MyAgent Unified Tool Registry

Version: 13.3.2
"""

from core.plugin_loader import load_plugins
# ==========================
# Intelligence Engine
# ==========================

from core.intelligence_router import intelligence
# ==========================
# Memory Tools
# ==========================

from core.memory_tools import (
    remember,
    recall,
    forget,
    show_memory,
)

# ==========================
# File Tools
# ==========================

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

# ==========================
# Project Tools
# ==========================

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

# ==========================
# Context Tools
# ==========================

from core.context_tools import (
    show_context,
    set_project_context,
    set_folder_context,
    set_file_context,
    set_mode,
    clear_context,
)

# ==========================
# Coding Engine
# ==========================

from core.coder_router import router
# ==========================
# Terminal Engine
# ==========================

from core.terminal_router import terminal_router
# ==========================
# System Tools
# ==========================

from core.system_check import system_check


TOOLS = {

    # ======================
    # Memory
    # ======================

    "remember": remember,
    "recall": recall,
    "forget": forget,
    "show_memory": show_memory,

    # ======================
    # Files
    # ======================

    "list_files": list_files,
    "create_folder": create_folder,
    "create_file": create_file,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,
    "delete_file": delete_file,
    "copy_file": copy_file,
    "run_command": run_command,

    # ======================
    # Projects
    # ======================

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

    # ======================
    # Context
    # ======================

    "show_context": show_context,
    "set_project_context": set_project_context,
    "set_folder_context": set_folder_context,
    "set_file_context": set_file_context,
    "set_mode": set_mode,
    "clear_context": clear_context,

    # ======================
    # Coding Engine
    # ======================

    "create_code_project": router.create_project,
    "build_website": router.build_website,
    "scan_project": router.scan,
    "read_code_file": router.read,
    "write_code_file": router.overwrite,

    # ======================
    # Terminal Engine
    # ======================

    "terminal_command": terminal_router.command,
    "git_status": terminal_router.git_status,
    "git_branch": terminal_router.git_branch,
    "git_log": terminal_router.git_log,
    "git_add": terminal_router.git_add,
    "git_commit": terminal_router.git_commit,
    "pip_install": terminal_router.pip_install,
    "pip_uninstall": terminal_router.pip_uninstall,
    "npm_install": terminal_router.npm_install,
    "npm_package": terminal_router.npm_package,    # ======================
    # System
    # ======================
    # ======================
    # Intelligence Engine
    # ======================

    "analyze_code_file": intelligence.analyze_file,
    "index_code_project": intelligence.index_project,
    "scan_dependencies": intelligence.scan_dependencies,
    "project_summary": intelligence.project_summary,
    "system_check": system_check,
}

# ==========================
# Load Plugin Tools
# ==========================

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
    Return all executable tools.
    """
    return sorted(TOOLS.keys())
