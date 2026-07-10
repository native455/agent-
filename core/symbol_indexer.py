"""
MyAgent Symbol Indexer

Version: 14.0.1
"""

from pathlib import Path

from core.code_analyzer import analyzer


class SymbolIndexer:

    def index_project(self, project):

        root = Path(project)

        if not root.exists():
            return {
                "success": False,
                "error": "Project not found."
            }

        symbols = []

        for file in root.rglob("*.py"):

            result = analyzer.analyze(str(file))

            if result.get("success"):

                symbols.append({
                    "file": str(file),
                    "classes": result["classes"],
                    "functions": result["functions"],
                })

        return {
            "success": True,
            "project": project,
            "files": len(symbols),
            "symbols": symbols,
        }


indexer = SymbolIndexer()
