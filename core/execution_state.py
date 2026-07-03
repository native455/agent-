"""
Execution State

MyAgent V12
"""

from datetime import datetime


def start_task(task):

    task["status"] = "running"

    task["started_at"] = datetime.now().isoformat()

    return task


def finish_task(task):

    task["status"] = "completed"

    task["finished_at"] = datetime.now().isoformat()

    start = datetime.fromisoformat(task["started_at"])
    end = datetime.fromisoformat(task["finished_at"])

    task["duration"] = round(
        (end - start).total_seconds(),
        3,
    )

    return task


def fail_task(task):

    task["status"] = "failed"

    task["finished_at"] = datetime.now().isoformat()

    start = datetime.fromisoformat(task["started_at"])
    end = datetime.fromisoformat(task["finished_at"])

    task["duration"] = round(
        (end - start).total_seconds(),
        3,
    )

    return 
