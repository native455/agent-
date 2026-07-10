"""
MyAgent Context Storage

Version: 13.1.0
"""

import json
from pathlib import Path

DATABASE = Path("data/context.json")


def ensure_database():

    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    if not DATABASE.exists():

        DATABASE.write_text(
            json.dumps(
                {
                    "project": None,
                    "folder": None,
                    "file": None,
                    "mode": "normal"
                },
                indent=4
            )
        )


def load_context():

    ensure_database()

    with open(DATABASE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_context(data):

    ensure_database()

    with open(DATABASE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
