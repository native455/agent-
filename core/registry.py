from tools import (
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

TOOLS = {
    "create_folder": create_folder,
    "create_file": create_file,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,
    "delete_file": delete_file,
    "copy_file": copy_file,
    "list_files": list_files,
    "run_command": run_command,
}

def execute_tool(task):
    tool_name = task["tool"]
    args = task.get("args", [])

    if tool_name not in TOOLS:
        return f"Unknown tool: {tool_name}"

    try:
        return TOOLS[tool_name](*args)
    except Exception as e:
        return f"Tool Error: {e}"
