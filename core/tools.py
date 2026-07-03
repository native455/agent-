"""
MyAgent Core Tools

Built-in filesystem and command utilities.
"""

import os
import shutil
import subprocess


def list_files(path="."):
    """List files in a directory."""
    return os.listdir(path)


def create_folder(name):
    """Create a folder."""
    os.makedirs(name, exist_ok=True)
    return f"Folder '{name}' created."


def create_file(filename):
    """Create an empty file."""
    with open(filename, "w", encoding="utf-8"):
        pass

    return f"File '{filename}' created."


def read_file(filename):
    """Read a text file."""

    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"{filename} does not exist."
        )

    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def write_file(filename, content):
    """Overwrite a file."""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Saved '{filename}'."


def append_file(filename, content):
    """Append text to a file."""

    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)

    return f"Appended to '{filename}'."


def delete_file(filename):
    """Delete a file."""

    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"{filename} does not exist."
        )

    os.remove(filename)

    return f"Deleted '{filename}'."


def copy_file(src, dst):
    """Copy a file."""

    if not os.path.exists(src):
        raise FileNotFoundError(
            f"{src} does not exist."
        )

    shutil.copy2(src, dst)

    return f"Copied '{src}' to '{dst}'."


def run_command(command):
    """Run a shell command."""

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            result.stderr.strip()
        )

    return result.stdout.strip()
