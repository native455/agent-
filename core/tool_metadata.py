"""
MyAgent Tool Metadata

Version: 12.4.1
"""

TOOL_METADATA = {}


def register_tool(name, description, arguments):
    """
    Register metadata for a tool.
    """

    TOOL_METADATA[name] = {
        "description": description,
        "arguments": arguments,
    }


def get_metadata(name):
    return TOOL_METADATA.get(name)


def all_metadata():
    return TOOL_METADATA
