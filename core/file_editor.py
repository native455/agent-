"""
MyAgent File Editor

Version: 13.3.1
"""

from pathlib import Path


class FileEditor:

    def read(self, filename):

        path = Path(filename)

        if not path.exists():
            return {
                "success": False,
                "error": "File not found."
            }

        return {
            "success": True,
            "content": path.read_text(
                encoding="utf-8"
            )
        }

    def overwrite(self, filename, content):

        path = Path(filename)

        path.write_text(
            content,
            encoding="utf-8"
        )

        return {
            "success": True,
            "message": "File updated."
        }


editor = FileEditor()
