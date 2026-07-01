"""
Plugin Loader

Loads all installed plugins.
"""

import importlib
from pathlib import Path

PLUGIN_DIR = Path("plugins")


def load_plugins():
    tools = {}

    if not PLUGIN_DIR.exists():
        return tools

    for plugin in PLUGIN_DIR.iterdir():

        # Ignore __pycache__ and non-plugin folders
        if (
            not plugin.is_dir()
            or plugin.name.startswith("__")
        ):
            continue

        # A valid plugin must contain plugin.py
        if not (plugin / "plugin.py").exists():
            continue

        try:
            module = importlib.import_module(
                f"plugins.{plugin.name}.plugin"
            )

            info = module.PLUGIN

            print(
                f"Loaded plugin: "
                f"{info['name']} "
                f"v{info['version']}"
            )

            tools.update(info["tools"])

        except Exception as e:
            print(f"Failed loading {plugin.name}: {e}")

    return tools
