"""
MyAgent Developer Console

Version: 11.1.0-dev
"""

from pathlib import Path

from plugins.plugin_manager.manager import (
    plugin_count,
    plugin_names,
)

from core.registry import list_available_tools
from core.health import health_report

from core.memory_db import (
    get_all_memory,
    memory_statistics,
)

VERSION_FILE = Path("VERSION")


def get_version():
    """Return the current project version."""

    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()

    return "Unknown"


def dashboard():
    """Display the developer dashboard."""

    print("=" * 60)
    print("           MyAgent Developer Console")
    print("=" * 60)

    print(f"Version          : {get_version()}")
    print("Status           : READY")
    print("Branch           : develop")
    print(f"Plugins Loaded   : {plugin_count()}")
    print(f"Available Tools  : {len(list_available_tools())}")

    print("=" * 60)

    print("1. List Plugins")
    print("2. List Tools")
    print("3. System Health")
    print("4. View Memory")
    print("5. Memory Statistics")
    print("6. Exit")


def list_plugins_menu():
    """Display installed plugins."""

    print("\nInstalled Plugins\n")

    for plugin in plugin_names():
        print(" -", plugin)

    input("\nPress Enter to continue...")


def list_tools_menu():
    """Display available tools."""

    print("\nAvailable Tools\n")

    for tool in list_available_tools():
        print(" -", tool)

    input("\nPress Enter to continue...")


def health_menu():
    """Display system health."""

    print("\nSystem Health\n")

    report = health_report()

    for key, value in report.items():
        print(f"{key:<18}: {value}")

    input("\nPress Enter to continue...")


def memory_menu():
    """Display all stored memories."""

    memories = get_all_memory()

    print("\nStored Memories\n")
    print("=" * 60)

    if not memories:
        print("No memories found.")
        input("\nPress Enter...")
        return

    for index, memory in enumerate(memories, start=1):

        print(f"[{index}]")
        print("ID       :", memory["id"])
        print("Category :", memory["category"])
        print("Title    :", memory["title"])
        print("Content  :", memory["content"])
        print("-" * 60)

    input("\nPress Enter...")


def statistics_menu():
    """Display memory statistics."""

    stats = memory_statistics()

    print("\nMemory Statistics\n")
    print("=" * 60)

    print(f"Total Memories : {stats['total']}")

    print("\nCategories\n")

    for category, count in stats["categories"].items():
        print(f"{category:<20}{count}")

    input("\nPress Enter...")


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
            memory_menu()

        elif choice == "5":
            statistics_menu()

        elif choice == "6":
            print("\nGoodbye.\n")
            break

        else:
            print("\nInvalid option.\n")


if __name__ == "__main__":
    main()
