"""
MyAgent Intelligence Router

Version: 14.0.3
"""

from core.code_analyzer import analyzer
from core.symbol_indexer import indexer
from core.dependency_scanner import scanner


class IntelligenceRouter:
    """
    Central entry point for all code-intelligence features.
    """

    def analyze_file(self, filename):
        return analyzer.analyze(filename)

    def index_project(self, project):
        return indexer.index_project(project)

    def scan_dependencies(self, project):
        return scanner.scan(project)

    def project_summary(self, project):

        symbols = self.index_project(project)
        deps = self.scan_dependencies(project)

        if not symbols.get("success"):
            return symbols

        if not deps.get("success"):
            return deps

        total_classes = 0
        total_functions = 0

        for item in symbols["symbols"]:
            total_classes += len(item["classes"])
            total_functions += len(item["functions"])

        return {
            "success": True,
            "project": project,
            "python_files": symbols["files"],
            "classes": total_classes,
            "functions": total_functions,
            "dependencies": deps["dependencies"],
        }


intelligence = IntelligenceRouter()
