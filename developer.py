import os
import subprocess
from datetime import datetime

VERSION_FILE = "VERSION"


def clear():
    os.system("clear")


def version():
    if not os.path.exists(VERSION_FILE):
        return "Unknown"

    with open(VERSION_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def run(cmd):
    print(f"\n$ {cmd}\n")
    subprocess.run(cmd, shell=True)


def self_test():

    print("\nRunning self-test...\n")

    files = [
        "agent.py",
        "config.py",
        "update.py",
        "core/ai.py",
        "core/router.py",
        "core/planner.py",
        "core/executor.py",
        "core/registry.py",
        "core/generator.py",
        "core/project_builder.py",
        "core/memory.py",
        "core/memory_tools.py",
    ]

    missing = []

    for file in files:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:")
        for m in missing:
            print("-", m)
    else:
        print("All required files exist.")

    print("\nChecking Python imports...\n")

    result = subprocess.run(
        "python -m py_compile agent.py",
        shell=True
    )

    if result.returncode == 0:
        print("Python compilation passed.")
    else:
        print("Compilation failed.")


def backup():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"MyAgent_{timestamp}.zip"

    print("Creating backup...")

    subprocess.run(
        f"zip -r {filename} .",
        shell=True
    )

    print("Backup saved as:")
    print(filename)


def menu():

    while True:

        clear()

        print("=" * 45)
        print("      MyAgent Developer Mode")
        print("=" * 45)
        print(f"Version: {version()}")
        print()

        print("1. Run Self Test")
        print("2. Backup Project")
        print("3. Git Status")
        print("4. Git Pull")
        print("5. Git Push")
        print("6. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            self_test()
            input("\nPress ENTER...")

        elif choice == "2":
            backup()
            input("\nPress ENTER...")

        elif choice == "3":
            run("git status")
            input("\nPress ENTER...")

        elif choice == "4":
            run("git pull")
            input("\nPress ENTER...")

        elif choice == "5":
            run("git push")
            input("\nPress ENTER...")

        elif choice == "6":
            break


if __name__ == "__main__":
    menu()
