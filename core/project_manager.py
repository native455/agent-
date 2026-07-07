"""
MyAgent Project Manager

Version: 13.0.0
"""

from pathlib import Path

from core.project_storage import (
    load_database,
    save_database,
)


PROJECT_ROOT = Path("Projects")


class ProjectManager:

    def __init__(self):

        PROJECT_ROOT.mkdir(exist_ok=True)

    def create(self, name):

        db = load_database()

        if name in db["projects"]:
            return False, "Project already exists."

        project = PROJECT_ROOT / name

        (project / "src").mkdir(parents=True, exist_ok=True)
        (project / "assets").mkdir(exist_ok=True)
        (project / "tests").mkdir(exist_ok=True)

        (project / "README.md").write_text(
            f"# {name}\n",
            encoding="utf-8"
        )

        (project / "todo.md").write_text(
            "",
            encoding="utf-8"
        )

        (project / "notes.md").write_text(
            "",
            encoding="utf-8"
        )

        db["projects"][name] = {
            "tasks": [],
            "notes": []
        }

        db["active"] = name

        save_database(db)

        return True, f"Project '{name}' created."

    def list_projects(self):

        db = load_database()

        return sorted(db["projects"].keys())

    def active(self):

        return load_database()["active"]

    def open(self, name):

        db = load_database()

        if name not in db["projects"]:
            return False, "Project not found."

        db["active"] = name

        save_database(db)

        return True, f"Opened '{name}'."

    def close(self):

        db = load_database()

        db["active"] = None

        save_database(db)

        return True, "Project closed."


project_manager = ProjectManager()
