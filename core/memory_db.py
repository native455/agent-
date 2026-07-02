"""
Memory Database

MyAgent Memory V3

Version: 1.2.0
"""

import json
import uuid
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("data/memory.json")


def ensure_database():
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not MEMORY_FILE.exists():
        MEMORY_FILE.write_text("[]", encoding="utf-8")


def save_memory(data):
    ensure_database()

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_memory():
    ensure_database()

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Already V3 format
    if isinstance(data, list):
        return data

    # Migrate old dictionary format
    if isinstance(data, dict):
        memories = []

        for key, value in data.items():
            memories.append({
                "id": str(uuid.uuid4()),
                "category": "legacy",
                "title": key,
                "content": str(value),
                "created": datetime.now().isoformat(),
                "updated": datetime.now().isoformat()
            })

        save_memory(memories)
        return memories

    return []


def add_memory(category, title, content):
    memory = load_memory()

    entry = {
        "id": str(uuid.uuid4()),
        "category": category,
        "title": title,
        "content": content,
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }

    memory.append(entry)

    save_memory(memory)

    return entry


def get_all_memory():
    return load_memory()


def get_memory(memory_id):
    memory = load_memory()

    for entry in memory:
        if entry["id"] == memory_id:
            return entry

    return None


def update_memory(memory_id, **updates):
    memory = load_memory()

    for entry in memory:

        if entry["id"] == memory_id:

            for key, value in updates.items():
                if key in entry:
                    entry[key] = value

            entry["updated"] = datetime.now().isoformat()

            save_memory(memory)

            return entry

    return None


def delete_memory(memory_id):
    memory = load_memory()

    new_memory = [
        entry
        for entry in memory
        if entry["id"] != memory_id
    ]

    if len(new_memory) == len(memory):
        return False

    save_memory(new_memory)

    return True
def search_memory(keyword):
    """
    Search memories by title or content.
    """

    keyword = keyword.lower()

    results = []

    for entry in load_memory():

        if (
            keyword in entry["title"].lower()
            or keyword in entry["content"].lower()
        ):
            results.append(entry)

    return results


def search_category(category):
    """
    Search memories by category.
    """

    category = category.lower()

    return [
        entry
        for entry in load_memory()
        if entry["category"].lower() == category
    ]


def memory_statistics():
    """
    Return memory statistics.
    """

    memory = load_memory()

    categories = {}

    for entry in memory:

        cat = entry["category"]

        categories[cat] = categories.get(cat, 0) + 1

    return {
        "total": len(memory),
        "categories": categories
    }
