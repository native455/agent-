"""
MyAgent Executor

Version: 13.0.2
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

    # Automatically assign IDs
    for index, task in enumerate(plan, start=1):
        task.setdefault("id", index)

    for task in plan:

        print(f"[{task['id']}/{total}] {task['tool']}")

        start_task(task)

        success, tool_result, attempts = retry(
            execute_tool,
            task
        )

        # Tool executed successfully
        if success:

            finish_task(task)

            # New-style tool result
            if isinstance(tool_result, dict):

                if tool_result.get("success", True):
                    output = tool_result.get(
                        "data",
                        tool_result.get("message", "")
                    )
                else:
                    output = tool_result.get(
                        "error",
                        "Unknown error."
                    )

            # Old-style tool result (string, list, etc.)
            else:
                output = tool_result

        else:

            fail_task(task)

            output = str(tool_result)

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
