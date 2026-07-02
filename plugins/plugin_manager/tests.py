"""
Plugin Manager Tests

Version: 1.0.0
"""

from plugins.plugin_manager.manager import (
    list_plugins,
    plugin_count,
    plugin_names,
)


def run_tests():

    print("=" * 40)
    print("Plugin Manager Test Suite")
    print("=" * 40)

    plugins = list_plugins()

    assert isinstance(plugins, list)

    count = plugin_count()

    assert count >= 2

    names = plugin_names()

    assert "filesystem" in names
    assert "plugin_manager" in names

    print(f"Installed Plugins : {count}")

    print("Plugin Names:")

    for name in names:
        print(" -", name)

    print("\n✅ Plugin Manager tests passed.")


if __name__ == "__main__":
    run_tests()
