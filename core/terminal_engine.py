"""
MyAgent Terminal Engine

Version: 13.4.0
"""

import subprocess

from core.command_guard import validate


class TerminalEngine:

    def run(self, command):

        allowed, reason = validate(command)

        if not allowed:
            return {
                "success": False,
                "error": reason,
            }

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }


terminal = TerminalEngine()
