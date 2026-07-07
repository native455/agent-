"""
MyAgent Intent Router

Version: 12.4.0

Routes common requests without calling AI.
"""

import re


def route(user):

    text = user.strip()

    # Remember my name is Okechukwu
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
                "args": [key, value]
            }
        ]

    # What is my name?
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
                "args": [key]
            }
        ]

    # Read VERSION
    m = re.match(
        r"read (.+)",
        text,
        re.IGNORECASE,
    )

    if m:

        return [
            {
                "tool": "read_file",
                "args": [m.group(1).strip()]
            }
        ]

    # List files
    if text.lower() == "list files":

        return [
            {
                "tool": "list_files",
                "args": []
            }
        ]

    # No simple intent found
    return None
