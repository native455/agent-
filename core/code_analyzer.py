"""
MyAgent Code Analyzer

Version: 14.0.0
"""

import ast
from pathlib import Path


class CodeAnalyzer:

    def analyze(self, filename):

        path = Path(filename)

        if not path.exists():
            return {
                "success": False,
                "error": "File not found."
            }

        source = path.read_text(
            encoding="utf-8"
        )

        tree = ast.parse(source)

        classes = []
        functions = []
        imports = []

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)

            elif isinstance(node, ast.Import):
                for item in node.names:
                    imports.append(item.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                imports.append(module)

        return {
            "success": True,
            "file": filename,
            "classes": sorted(classes),
            "functions": sorted(functions),
            "imports": sorted(set(imports)),
        }


analyzer = CodeAnalyzer()
