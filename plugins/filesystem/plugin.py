"""
Filesystem Plugin

Plugin entry point for MyAgent.

Version: 1.0.0
"""

from plugins.filesystem.file_ops import (
    create_file,
    read_file,
    write_file,
    append_file,
    delete_file,
    rename_file,
    copy_file,
    move_file,
)

from plugins.filesystem.search import (
    search_files,
    search_extension,
)

PLUGIN = {
    "name": "filesystem",
    "version": "1.0.0",
    "author": "MyAgent Development Team",
    "description": "Safe filesystem operations for MyAgent.",

    "tools": {
        "create_file": create_file,
        "read_file": read_file,
        "write_file": write_file,
        "append_file": append_file,
        "delete_file": delete_file,
        "rename_file": rename_file,
        "copy_file": copy_file,
        "move_file": move_file,
        "search_files": search_files,
        "search_extension": search_extension,
    }
}
