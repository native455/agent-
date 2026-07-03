from core.memory_db import (
    add_memory,
    get_all_memory,
    search_memory,
    delete_memory,
)


def remember(key, value):
    add_memory(
        "memory",
        key,
        value,
    )

    return f"I'll remember that {key} = {value}"


def recall(key):

    results = search_memory(key)

    if not results:
        return "I don't know."

    return results[-1]["content"]


def forget(key):

    results = search_memory(key)

    if not results:
        return "Nothing to forget."

    delete_memory(results[-1]["id"])

    return f"Forgot {key}."


def show_memory():

    memories = get_all_memory()

    if not memories:
        return "Memory is empty."

    lines = []

    for item in memories:
        lines.append(
            f"{item['title']} = {item['content']}"
        )

    return "\n".join(lines)
