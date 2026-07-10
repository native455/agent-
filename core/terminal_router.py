"""
MyAgent Terminal Router

Version: 13.4.1
"""

from core.terminal_engine import terminal
from core.git_engine import git
from core.package_manager import packages


class TerminalRouter:

    def command(self, command):
        return terminal.run(command)

    def git_status(self):
        return git.status()

    def git_branch(self):
        return git.branch()

    def git_log(self):
        return git.log()

    def git_add(self):
        return git.add_all()

    def git_commit(self, message):
        return git.commit(message)

    def pip_install(self, package):
        return packages.pip_install(package)

    def pip_uninstall(self, package):
        return packages.pip_uninstall(package)

    def npm_install(self):
        return packages.npm_install()

    def npm_package(self, package):
        return packages.npm_package(package)


terminal_router = TerminalRouter()
