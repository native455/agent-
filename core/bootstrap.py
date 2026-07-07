"""
MyAgent Bootstrap

Version: 12.4.3

Initializes the system.
"""

from core.register_builtin_tools import register_builtin_tools


_INITIALIZED = False


def bootstrap():
    """
    Initialize MyAgent once.
    """

    global _INITIALIZED

    if _INITIALIZED:
        return

    register_builtin_tools()

    _INITIALIZED = True
