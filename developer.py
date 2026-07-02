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

VERSION_FILE = Path("VERSION")


def get_version():
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()
    return "Unknown"


def dashboard():

    print("=" * 50)
    print("        MyAgent Developer Console")
    print("=" * 50)

    print(f"Version          : {get_version()}")
    print("Status           : READY")
    print("Branch           : develop")

    print(f"Plugins Loaded   : {plugin_count()}")

    print(
        f"Available Tools  : {len(list_available_tools())}"
    )

    print("=" * 50)

    print("1. List Plugins")
    print("2. List Tools")
    print("3. Exit")


def main():

    while True:

        dashboard()

        choice = input("\nSelect: ").strip()

        if choice == "1":

            print("\nInstalled Plugins\n")

            for plugin in plugin_names():
                print(" -", plugin)

            input("\nPress Enter...")

        elif choice == "2":

            print("\nAvailable Tools\n")

            for tool in list_available_tools():
                print(" -", tool)

            input("\nPress Enter...")

        elif choice == "3":

            print("\nGoodbye.\n")
            break

        else:

            print("\nInvalid option.\n")


if __name__ == "__main__":
    main()
