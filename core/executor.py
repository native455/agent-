"""
MyAgent Executor

Version: 14.1.0
"""

from core.logger import logger
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

        logger.info(
            f"Starting task: {task['tool']} {task.get('args', [])}"
        )

        success, tool_result, attempts = retry(
            execute_tool,
            task
        )

        if success:

            finish_task(task)

            logger.info(
                f"Completed task: {task['tool']}"
            )

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

            else:

                output = tool_result

        else:

            fail_task(task)

            logger.error(
                f"Task failed: {task['tool']}"
            )

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
