"""
Health Monitor

Checks the status of MyAgent components.

Version: 11.0.0-dev
"""

import platform
from pathlib import Path

from plugins.plugin_manager.manager import plugin_count
from core.registry import list_available_tools


def health_report():
    """
    Return a dictionary containing the current
    health status of MyAgent.
    """

    version_file = Path("VERSION")

    if version_file.exists():
        version = version_file.read_text().strip()
    else:
        version = "Unknown"

    report = {
        "Python": platform.python_version(),
        "Version": version,
        "Plugins": plugin_count(),
        "Tools": len(list_available_tools()),
        "Data Folder": Path("data").exists(),
        "Memory File": (
            Path("memory.json").exists()
            or Path("data/memory.json").exists()
        ),
    }

    return report
