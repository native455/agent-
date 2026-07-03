"""
MyAgent Core Tools

Version: 12.0.0
"""

import os
import shutil
import subprocess

from core.tool_result import (
    success_result,
    error_result,
)


def list_files(path="."):
    try:
        return success_result(
            "list_files",
            os.listdir(path),
        )
    except Exception as e:
        return error_result("list_files", e)


def create_folder(name):
    try:
        os.makedirs(name, exist_ok=True)
        return success_result(
            "create_folder",
            f"Folder '{name}' created."
        )
    except Exception as e:
        return error_result("create_folder", e)


def create_file(filename):
    try:
        with open(filename, "w", encoding="utf-8"):
            pass

        return success_result(
            "create_file",
            f"File '{filename}' created."
        )

    except Exception as e:
        return error_result("create_file", e)


def read_file(filename):
    try:

        if not os.path.exists(filename):
            raise FileNotFoundError(
                f"{filename} does not exist."
            )

        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()

        return success_result(
            "read_file",
            data
        )

    except Exception as e:
        return error_result("read_file", e)


def write_file(filename, content):
    try:

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        return success_result(
            "write_file",
            f"Saved '{filename}'."
        )

    except Exception as e:
        return error_result("write_file", e)


def append_file(filename, content):
    try:

        with open(filename, "a", encoding="utf-8") as f:
            f.write(content)

        return success_result(
            "append_file",
            f"Appended to '{filename}'."
        )

    except Exception as e:
        return error_result("append_file", e)


def delete_file(filename):
    try:

        if not os.path.exists(filename):
            raise FileNotFoundError(
                f"{filename} does not exist."
            )

        os.remove(filename)

        return success_result(
            "delete_file",
            f"Deleted '{filename}'."
        )

    except Exception as e:
        return error_result("delete_file", e)


def copy_file(src, dst):
    try:

        if not os.path.exists(src):
            raise FileNotFoundError(
                f"{src} does not exist."
            )

        shutil.copy2(src, dst)

        return success_result(
            "copy_file",
            f"Copied '{src}' to '{dst}'."
        )

    except Exception as e:
        return error_result("copy_file", e)


def run_command(command):
    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())

        return success_result(
            "run_command",
            result.stdout.strip(),
        )

    except Exception as e:
        return error_result("run_command", e)
