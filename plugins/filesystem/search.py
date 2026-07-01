"""
Filesystem Plugin

Search Module

Provides recursive file searching.

Version: 1.0.0
"""

from pathlib import Path


def search_files(pattern: str, root: str = ".") -> list[str]:
    """
    Search recursively for files whose names contain
    the supplied pattern.

    Example:

    search_files("py")
    """

    results = []

    root_path = Path(root)

    for file in root_path.rglob("*"):

        if file.is_file():

            if pattern.lower() in file.name.lower():

                results.append(str(file))

    return sorted(results)


def search_extension(extension: str, root: str = ".") -> list[str]:
    """
    Search by extension.

    Example:

    search_extension(".py")
    """

    results = []

    root_path = Path(root)

    if not extension.startswith("."):
        extension = "." + extension

    for file in root_path.rglob(f"*{extension}"):

        if file.is_file():

            results.append(str(file))

    return sorted(results)
