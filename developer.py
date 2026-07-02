"""
MyAgent Developer Console

Version: 11.0.0-dev
"""

from pathlib import Path

from plugins.plugin_manager.manager import (
    plugin_count,
    plugin_names,
)

from core.registry import list_available_tools
from core.health import health_report

VERSION_FILE = Path("VERSION")


def get_version():
    """Return the current project version."""

    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()

    return "Unknown"


def dashboard():
    """Display the developer dashboard."""

    print("=" * 50)
    print("        MyAgent Developer Console")
    print("=" * 50)

    print(f"Version          : {get_version()}")
    print("Status           : READY")
    print("Branch           : develop")
    print(f"Plugins Loaded   : {plugin_count()}")
    print(f"Available Tools  : {len(list_available_tools())}")

    print("=" * 50)

    print("1. List Plugins")
    print("2. List Tools")
    print("3. System Health")
    print("4. Exit")


def list_plugins_menu():
    """Display installed plugins."""

    print("\nInstalled Plugins\n")

    for plugin in plugin_names():
        print(" -", plugin)

    input("\nPress Enter to continue...")


def list_tools_menu():
    """Display registered tools."""

    print("\nAvailable Tools\n")

    for tool in list_available_tools():
        print(" -", tool)

    input("\nPress Enter to continue...")


def health_menu():
    """Display health information."""

    print("\nSystem Health\n")

    report = health_report()

    for key, value in report.items():
        print(f"{key:<15}: {value}")

    input("\nPress Enter to continue...")


def main():

    while True:

        dashboard()

        choice = input("\nSelect: ").strip()

        if choice == "1":
            list_plugins_menu()

        elif choice == "2":
            list_tools_menu()

        elif choice == "3":
            health_menu()

        elif choice == "4":
            print("\nGoodbye.\n")
            break

        else:
            print("\nInvalid option.\n")


if __name__ == "__main__":
    main()
