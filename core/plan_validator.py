"""
Plan Validator

MyAgent V15.0.0
"""


def validate_plan(plan):
    """
    Ensures every planner task has the correct format.

    Returns a cleaned plan.
    """

    if not isinstance(plan, list):
        return []

    cleaned = []

    for item in plan:

        if not isinstance(item, dict):
            continue

        tool = item.get("tool")

        if not tool:
            continue

        args = item.get("args", [])

        if args is None:
            args = []

        if not isinstance(args, list):
            args = [args]

        cleaned.append(
            {
                "tool": tool,
                "args": args,
            }
        )

    return cleaned
