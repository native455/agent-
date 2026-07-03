"""
MyAgent Executor

Version: 12.0.0
"""

from core.registry import execute_tool
from core.execution_state import (
    start_task,
    finish_task,
    fail_task,
)
from core.retry import retry
from core.plan_history import record_plan


def execute_plan(plan, goal="Unknown Task"):

    results = []

    total = len(plan)

    for task in plan:

        print(f"[{task['id']}/{total}] {task['tool']}")

        start_task(task)

        success, tool_result, attempts = retry(
            execute_tool,
            task
        )

        # Retry engine itself failed
        if not success:

            fail_task(task)

            results.append(
                {
                    "id": task["id"],
                    "tool": task["tool"],
                    "status": task["status"],
                    "attempts": attempts,
                    "started_at": task["started_at"],
                    "finished_at": task["finished_at"],
                    "duration": task["duration"],
                    "result": str(tool_result),
                }
            )

            continue

        # Tool Result API
        if tool_result["success"]:

            finish_task(task)

            output = tool_result["data"]

        else:

            fail_task(task)

            output = tool_result["error"]

        results.append(
            {
                "id": task["id"],
                "tool": task["tool"],
                "status": task["status"],
                "attempts": attempts,
                "started_at": task["started_at"],
                "finished_at": task["finished_at"],
                "duration": task["duration"],
                "result": output,
            }
        )

    record_plan(goal, results)

    return results
