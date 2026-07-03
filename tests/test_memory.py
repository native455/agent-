"""
Memory Test Suite

Version: 11.1.0-dev
"""

from core.memory_db import (
    add_memory,
    get_memory,
    update_memory,
    delete_memory,
    search_memory,
    search_category,
    memory_statistics,
)


def run_tests():

    print("=" * 50)
    print("Memory Test Suite")
    print("=" * 50)

    memory = add_memory(
        "test",
        "Memory Test",
        "Testing Memory V3"
    )

    memory_id = memory["id"]

    assert get_memory(memory_id) is not None

    update_memory(
        memory_id,
        content="Updated"
    )

    assert get_memory(memory_id)["content"] == "Updated"

    assert len(search_memory("updated")) >= 1

    assert len(search_category("test")) >= 1

    stats = memory_statistics()

    assert "total" in stats
    assert "categories" in stats

    assert delete_memory(memory_id)

    assert get_memory(memory_id) is None

    print("\n✅ Memory tests passed.")


if __name__ == "__main__":
    run_tests()
