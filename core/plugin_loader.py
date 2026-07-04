"""
MyAgent Plugin Loader

Version: 12.2.0
"""

import importlib
from pathlib import Path

from core.sdk import registered_tools

PLUGIN_DIR = Path("plugins")


def load_plugins():
    """
    Load legacy plugins and SDK plugins.
    """

    tools = {}

    if not PLUGIN_DIR.exists():
        return tools

    for plugin in PLUGIN_DIR.iterdir():

        if not plugin.is_dir():
            continue

        if plugin.name.startswith("__"):
            continue

        if not (plugin / "plugin.py").exists():
            continue

        try:

            module = importlib.import_module(
                f"plugins.{plugin.name}.plugin"
            )

            # Legacy plugin support
            if hasattr(module, "PLUGIN"):

                info = module.PLUGIN

                print(
                    f"Loaded plugin: "
                    f"{info['name']} "
                    f"v{info['version']}"
                )

                tools.update(info["tools"])

            # SDK plugin support
            sdk_tools = registered_tools()

            for name, info in sdk_tools.items():

                if name not in tools:

                    tools[name] = info["function"]

                    print(
                        f"Loaded SDK Tool: {name}"
                    )

        except Exception as e:

            print(
                f"Failed loading {plugin.name}: {e}"
            )

    return tools
