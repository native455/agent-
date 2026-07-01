import importlib
import os

PLUGIN_FOLDER = "plugins"


def load_plugins():
    loaded = {}

    if not os.path.exists(PLUGIN_FOLDER):
        os.makedirs(PLUGIN_FOLDER)
        return loaded

    for filename in os.listdir(PLUGIN_FOLDER):

        if not filename.endswith(".py"):
            continue

        if filename.startswith("__"):
            continue

        module_name = filename[:-3]

        try:
            module = importlib.import_module(f"plugins.{module_name}")

            if hasattr(module, "TOOLS"):

                loaded.update(module.TOOLS)

                print(f"Loaded plugin: {module_name}")

        except Exception as e:

            print(f"Plugin {module_name} failed: {e}")

    return loaded
