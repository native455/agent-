"""
MyAgent System Manager

Version: 12.4.5
"""

from core.system_check import system_check
from core.capability_registry import capabilities
from core.registry import list_available_tools


def system_report():
    """
    Return a complete system report.
    """

    return {
        "health": system_check(),
        "tool_count": len(list_available_tools()),
        "tools": list_available_tools(),
        "capabilities": capabilities(),
    }
