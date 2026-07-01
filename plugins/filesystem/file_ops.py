"""
Filesystem Plugin

File Operations Module

Provides safe filesystem operations for MyAgent.

Version: 1.0.0
"""

from pathlib import Path
import shutil


def create_file(path: str) -> str:
    """Create an empty file."""

    file = Path(path)

    file.parent.mkdir(parents=True, exist_ok=True)

    file.touch(exist_ok=True)

    return f"Created: {file}"


def read_file(path: str) -> str:
    """Read a text file."""

    file = Path(path)

    if not file.exists():
        return "File not found."

    return file.read_text(encoding="utf-8")


def write_file(path: str, content: str) -> str:
    """Overwrite a file."""

    file = Path(path)

    file.parent.mkdir(parents=True, exist_ok=True)

    file.write_text(content, encoding="utf-8")

    return f"Written: {file}"


def append_file(path: str, content: str) -> str:
    """Append text."""

    file = Path(path)

    file.parent.mkdir(parents=True, exist_ok=True)

    with open(file, "a", encoding="utf-8") as f:
        f.write(content)

    return f"Updated: {file}"


def delete_file(path: str) -> str:
    """Delete a file."""

    file = Path(path)

    if not file.exists():
        return "File not found."

    file.unlink()

    return f"Deleted: {file}"


def rename_file(old: str, new: str) -> str:
    """Rename a file."""

    old_file = Path(old)

    if not old_file.exists():
        return "File not found."

    new_file = Path(new)

    old_file.rename(new_file)

    return f"Renamed to {new_file}"


def copy_file(src: str, dst: str) -> str:
    """Copy a file."""

    source = Path(src)

    if not source.exists():
        return "File not found."

    destination = Path(dst)

    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source, destination)

    return f"Copied to {destination}"


def move_file(src: str, dst: str) -> str:
    """Move a file."""

    source = Path(src)

    if not source.exists():
        return "File not found."

    destination = Path(dst)

    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.move(str(source), str(destination))

    return f"Moved to {destination}"
