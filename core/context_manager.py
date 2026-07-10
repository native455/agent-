"""
MyAgent Context Manager

Version: 13.1.0
"""

from core.context_storage import (
    load_context,
    save_context,
)


class ContextManager:

    def get(self):
        """
        Return the current context.
        """
        return load_context()

    def set_project(self, project):
        data = load_context()
        data["project"] = project
        save_context(data)
        return f"Active project set to '{project}'."

    def set_folder(self, folder):
        data = load_context()
        data["folder"] = folder
        save_context(data)
        return f"Active folder set to '{folder}'."

    def set_file(self, filename):
        data = load_context()
        data["file"] = filename
        save_context(data)
        return f"Active file set to '{filename}'."

    def set_mode(self, mode):
        data = load_context()
        data["mode"] = mode
        save_context(data)
        return f"Mode changed to '{mode}'."

    def clear(self):
        data = {
            "project": None,
            "folder": None,
            "file": None,
            "mode": "normal",
        }
        save_context(data)
        return "Context cleared."


context_manager = ContextManager()
