"""
MyAgent Project Tools

Version: 13.0.0
"""

from core.project_manager import project_manager
from core.project_storage import (
    load_database,
    save_database,
)


def create_project(name):
    success, message = project_manager.create(name)
    return message


def open_project(name):
    success, message = project_manager.open(name)
    return message


def close_project():
    success, message = project_manager.close()
    return message


def list_projects():
    projects = project_manager.list_projects()

    if not projects:
        return "No projects found."

    return "\n".join(projects)


def project_status():
    active = project_manager.active()

    if active is None:
        return "No active project."

    db = load_database()

    info = db["projects"][active]

    return (
        f"Active Project : {active}\n"
        f"Tasks          : {len(info['tasks'])}\n"
        f"Notes          : {len(info['notes'])}"
    )


def add_task(task):

    db = load_database()

    active = db["active"]

    if active is None:
        return "No active project."

    db["projects"][active]["tasks"].append(
        {
            "title": task,
            "completed": False,
        }
    )

    save_database(db)

    return f"Task added to {active}."


def show_tasks():

    db = load_database()

    active = db["active"]

    if active is None:
        return "No active project."

    tasks = db["projects"][active]["tasks"]

    if not tasks:
        return "No tasks."

    output = []

    for i, task in enumerate(tasks, start=1):

        mark = "✓" if task["completed"] else " "

        output.append(f"[{mark}] {i}. {task['title']}")

    return "\n".join(output)


def complete_task(index):

    db = load_database()

    active = db["active"]

    if active is None:
        return "No active project."

    tasks = db["projects"][active]["tasks"]

    if index < 1 or index > len(tasks):
        return "Invalid task number."

    tasks[index - 1]["completed"] = True

    save_database(db)

    return "Task completed."


def add_note(note):

    db = load_database()

    active = db["active"]

    if active is None:
        return "No active project."

    db["projects"][active]["notes"].append(note)

    save_database(db)

    return "Note added."


def show_notes():

    db = load_database()

    active = db["active"]

    if active is None:
        return "No active project."

    notes = db["projects"][active]["notes"]

    if not notes:
        return "No notes."

    return "\n".join(f"- {note}" for note in notes)
