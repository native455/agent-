"""
Plugin Manager Plugin

Entry point.

Version: 1.0.0
"""

from plugins.plugin_manager.manager import (
    list_plugins,
    plugin_count,
    plugin_names,
)

PLUGIN = {
    "name": "plugin_manager",
    "version": "1.0.0",
    "author": "MyAgent Development Team",
    "description": "Manage installed plugins.",

    "tools": {
        "list_plugins": list_plugins,
        "plugin_count": plugin_count,
        "plugin_names": plugin_names,
    }
}
