"""
Plugin Manager

Core plugin management functions.

Version: 1.0.0
"""

from pathlib import Path
import importlib

PLUGIN_DIR = Path("plugins")


def list_plugins():
    """
    Return information about every installed plugin.
    """

    plugins = []

    if not PLUGIN_DIR.exists():
        return plugins

    for folder in sorted(PLUGIN_DIR.iterdir()):

        if (
            not folder.is_dir()
            or folder.name.startswith("__")
        ):
            continue

        plugin_file = folder / "plugin.py"

        if not plugin_file.exists():
            continue

        try:

            module = importlib.import_module(
                f"plugins.{folder.name}.plugin"
            )

            info = module.PLUGIN

            plugins.append({
                "name": info.get("name"),
                "version": info.get("version"),
                "description": info.get("description", ""),
                "author": info.get("author", "Unknown"),
            })

        except Exception as e:

            plugins.append({
                "name": folder.name,
                "error": str(e)
            })

    return plugins


def plugin_count():
    """Return the number of installed plugins."""
    return len(list_plugins())


def plugin_names():
    """Return only the plugin names."""
    return [
        plugin["name"]
        for plugin in list_plugins()
        if "name" in plugin
    ]
