"""
MyAgent Intelligent Router
"""

SHELL_COMMANDS = (
    "ls",
    "pwd",
    "cat",
    "mkdir",
    "touch",
    "rm",
    "cp",
    "mv",
    "python",
    "git",
    "pip",
)

MEMORY_COMMANDS = (
    "remember",
    "forget",
    "show memory",
    "what is my",
    "what's my",
)

PLANNER_COMMANDS = (
    "build",
    "create",
    "write",
    "delete",
    "copy",
    "read",
    "list",
)


def decide(user):

    text = user.lower().strip()

    if text.startswith(SHELL_COMMANDS):
        return []

    if text.startswith(MEMORY_COMMANDS):
        from core.planner import plan_task
        return plan_task(user)

    if text.startswith(PLANNER_COMMANDS):
        from core.planner import plan_task
        return plan_task(user)

    return []
