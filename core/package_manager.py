"""
MyAgent Package Manager

Version: 13.4.1
"""

from core.terminal_engine import terminal


class PackageManager:

    def pip_install(self, package):
        return terminal.run(
            f"pip install {package}"
        )

    def pip_uninstall(self, package):
        return terminal.run(
            f"pip uninstall -y {package}"
        )

    def npm_install(self):
        return terminal.run("npm install")

    def npm_package(self, package):
        return terminal.run(
            f"npm install {package}"
        )


packages = PackageManager()
