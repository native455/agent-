"""
MyAgent Plugin SDK

Version: 12.2.0
"""

TOOL_REGISTRY = {}


def tool(name, description=""):
    """
    Register a function as a MyAgent tool.
    """

    def decorator(func):

        TOOL_REGISTRY[name] = {
            "function": func,
            "description": description,
        }

        return func

    return decorator


def registered_tools():
    """
    Return all registered SDK tools.
    """
    return TOOL_REGISTRY
