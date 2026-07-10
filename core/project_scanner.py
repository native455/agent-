"""
MyAgent Project Scanner

Version: 13.3.1
"""

from pathlib import Path


class ProjectScanner:

    def scan(self, project):

        root = Path(project)

        if not root.exists():
            return {
                "success": False,
                "error": "Project not found."
            }

        files = []

        for file in root.rglob("*"):

            if file.is_file():

                files.append({
                    "name": file.name,
                    "path": str(file),
                    "extension": file.suffix.lower(),
                    "size": file.stat().st_size,
                })

        return {
            "success": True,
            "project": project,
            "count": len(files),
            "files": files,
        }


scanner = ProjectScanner()
