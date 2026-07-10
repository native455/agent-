"""
MyAgent Dependency Scanner

Version: 14.0.2
"""

from pathlib import Path

from core.code_analyzer import analyzer


class DependencyScanner:

    def scan(self, project):

        root = Path(project)

        if not root.exists():
            return {
                "success": False,
                "error": "Project not found."
            }

        dependencies = {}

        for file in root.rglob("*.py"):

            result = analyzer.analyze(str(file))

            if result.get("success"):

                dependencies[str(file)] = result["imports"]

        return {
            "success": True,
            "project": project,
            "dependencies": dependencies,
        }


scanner = DependencyScanner()
