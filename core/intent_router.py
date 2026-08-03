"""
MyAgent Intent Router

Version: 15.0.0

Routes common requests without calling AI.
"""

import re


def route(user):

    text = user.strip()
    lower = text.lower()

    # -------------------------
    # Memory
    # -------------------------

    m = re.match(
        r"remember my (.+?) is (.+)",
        text,
        re.IGNORECASE,
    )

    if m:

        key = (
            m.group(1)
            .strip()
            .lower()
            .replace(" ", "_")
        )

        value = m.group(2).strip()

        return [
            {
                "tool": "remember",
                "args": [key, value],
            }
        ]

    m = re.match(
        r"what is my (.+)",
        text,
        re.IGNORECASE,
    )

    if m:

        key = (
            m.group(1)
            .strip()
            .lower()
            .replace(" ", "_")
            .replace("?", "")
        )

        return [
            {
                "tool": "recall",
                "args": [key],
            }
        ]

    if lower == "show memory":

        return [
            {
                "tool": "show_memory",
                "args": [],
            }
        ]

    # -------------------------
    # Files
    # -------------------------

    m = re.match(
        r"read (.+)",
        text,
        re.IGNORECASE,
    )

    if m:

        return [
            {
                "tool": "read_file",
                "args": [m.group(1).strip()],
            }
        ]

    if lower == "list files":

        return [
            {
                "tool": "list_files",
                "args": [],
            }
        ]

    # -------------------------
    # Projects
    # -------------------------

    if lower == "list projects":

        return [
            {
                "tool": "list_projects",
                "args": [],
            }
        ]

    if lower == "show context":

        return [
            {
                "tool": "show_context",
                "args": [],
            }
        ]

    m = re.match(
        r"build (?:a )?website(?: called)? (.+)",
        text,
        re.IGNORECASE,
    )

    if m:

        return [
            {
                "tool": "build_website",
                "args": [m.group(1).strip()],
            }
        ]

    m = re.match(
        r"create project (.+)",
        text,
        re.IGNORECASE,
    )

    if m:

        return [
            {
                "tool": "create_project",
                "args": [m.group(1).strip()],
            }
        ]

    # -------------------------
    # No direct match
    # -------------------------

    return None
