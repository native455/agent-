"""
Tool Result API

MyAgent V12
"""


def success_result(tool, data=None, metadata=None):
    """
    Return a successful tool result.
    """

    return {
        "success": True,
        "data": data,
        "error": None,
        "metadata": {
            "tool": tool,
            **(metadata or {})
        }
    }


def error_result(tool, error, metadata=None):
    """
    Return a failed tool result.
    """

    return {
        "success": False,
        "data": None,
        "error": str(error),
        "metadata": {
            "tool": tool,
            **(metadata or {})
        }
    }
