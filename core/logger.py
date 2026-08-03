"""
MyAgent Logger

Version: 14.1.0
"""

from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "myagent.log"


class Logger:

    def log(self, level, message):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        line = (
            f"[{timestamp}] "
            f"[{level.upper()}] "
            f"{message}\n"
        )

        with open(
            LOG_FILE,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(line)

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def error(self, message):
        self.log("ERROR", message)

    def clear(self):

        LOG_FILE.write_text(
            "",
            encoding="utf-8"
        )


logger = Logger()
