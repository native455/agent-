"""
MyAgent Project Storage

Version: 13.0.0
"""

import json
from pathlib import Path

DATABASE = Path("data/projects.json")


def ensure_database():

    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    if not DATABASE.exists():

        DATABASE.write_text(
            json.dumps(
                {
                    "active": None,
                    "projects": {}
                },
                indent=4
            )
        )


def load_database():

    ensure_database()

    with open(DATABASE, "r") as f:
        return json.load(f)


def save_database(data):

    ensure_database()

    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)
