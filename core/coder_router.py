"""
MyAgent Coding Router

Version: 13.3.1
"""

from core.code_generator import generator
from core.project_builder import builder
from core.project_scanner import scanner
from core.file_editor import editor


class CodingRouter:

    def create_project(self, kind, name):
        return generator.generate(kind, name)

    def build_website(self, name):
        return builder.build_website(name)

    def scan(self, project):
        return scanner.scan(project)

    def read(self, filename):
        return editor.read(filename)

    def overwrite(self, filename, content):
        return editor.overwrite(
            filename,
            content,
        )


router = CodingRouter()
