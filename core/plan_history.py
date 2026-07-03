"""
Plan History

MyAgent V12
"""

import json
from pathlib import Path
from datetime import datetime

PLAN_FILE = Path("data/plans.json")


def ensure_database():

    PLAN_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not PLAN_FILE.exists():
        PLAN_FILE.write_text("[]", encoding="utf-8")


def load_history():

    ensure_database()

    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(history):

    ensure_database()

    with open(PLAN_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)


def record_plan(goal, results):

    history = load_history()

    history.append(
        {
            "goal": goal,
            "created": datetime.now().isoformat(),
            "results": results,
        }
    )

    save_history(history)


def all_plans():

    return load_history()


def latest_plan():

    history = load_history()

    if not history:
        return None

    return history[-1]
