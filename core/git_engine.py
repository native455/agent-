"""
MyAgent Git Engine

Version: 13.4.1
"""

from core.terminal_engine import terminal


class GitEngine:

    def status(self):
        return terminal.run("git status")

    def branch(self):
        return terminal.run("git branch")

    def log(self):
        return terminal.run("git log --oneline")

    def add_all(self):
        return terminal.run("git add .")

    def commit(self, message):
        return terminal.run(
            f'git commit -m "{message}"'
        )


git = GitEngine()
