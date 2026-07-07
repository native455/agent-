"""
MyAgent Capability Registry

Version: 12.4.2
"""

from core.tool_metadata import all_metadata


def capabilities():
    """
    Return all registered tool metadata.
    """
    return all_metadata()


def capability_prompt():
    """
    Build a planner-friendly description of all tools.
    """

    metadata = all_metadata()

    lines = []

    for name in sorted(metadata):

        tool = metadata[name]

        args = ", ".join(tool["arguments"])

        lines.append(
            f"- {name}({args}) : {tool['description']}"
        )

    return "\n".join(lines)
