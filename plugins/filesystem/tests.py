"""
Filesystem Plugin Tests

Version: 1.0.0
"""

from plugins.filesystem.file_ops import (
    create_file,
    write_file,
    read_file,
    append_file,
    delete_file,
)

from plugins.filesystem.search import (
    search_files,
    search_extension,
)


def run_tests():
    print("Running Filesystem Plugin Tests...\n")

    print(create_file("test_plugin.txt"))

    print(write_file("test_plugin.txt", "Hello"))

    assert read_file("test_plugin.txt") == "Hello"

    print(append_file("test_plugin.txt", "\nWorld"))

    assert "World" in read_file("test_plugin.txt")

    py_files = search_extension(".py")
    assert isinstance(py_files, list)

    results = search_files("agent")
    assert isinstance(results, list)

    print(delete_file("test_plugin.txt"))

    print("\n✅ All Filesystem Plugin tests passed.")


if __name__ == "__main__":
    run_tests()
