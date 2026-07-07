"""
MyAgent System Check

Version: 12.4.4
"""

from pathlib import Path

REQUIRED_FILES = [
    "agent.py",
    "core/router.py",
    "core/intent_router.py",
    "core/planner.py",
    "core/executor.py",
    "core/registry.py",
    "core/bootstrap.py",
    "core/tool_metadata.py",
    "core/capability_registry.py",
]


def system_check():
    """
    Check that all important project files exist.
    """

    report = {
        "status": "OK",
        "missing": [],
        "checked": len(REQUIRED_FILES),
    }

    for filename in REQUIRED_FILES:

        if not Path(filename).exists():
            report["missing"].append(filename)

    if report["missing"]:
        report["status"] = "ERROR"

    return report
