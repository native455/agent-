"""
MyAgent Command Guard

Version: 13.4.0
"""

SAFE_PREFIXES = [
    "python",
    "python3",
    "pip",
    "pip3",
    "pytest",
    "git",
    "ls",
    "pwd",
    "echo",
    "cat",
    "whoami",
    "uname",
    "npm",
    "node",
]

BLOCKED_WORDS = [
    "rm -rf",
    "mkfs",
    "shutdown",
    "reboot",
    "poweroff",
    "dd ",
    "chmod 777",
]


def validate(command):

    command = command.strip()

    lower = command.lower()

    for word in BLOCKED_WORDS:
        if word in lower:
            return (
                False,
                f"Blocked dangerous command: {word}"
            )

    if not any(
        lower.startswith(prefix)
        for prefix in SAFE_PREFIXES
    ):
        return (
            False,
            "Command not on safe allow-list."
        )

    return True, "OK"
