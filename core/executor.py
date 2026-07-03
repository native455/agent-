"""
MyAgent Executor

Planner V3 Execution Engine
"""

from core.registry import execute_tool

from core.execution_state import (
    start_task,
    finish_task,
    fail_task,
)


def execute_plan(plan):

    results = []

    total = len(plan)

    for task in plan:

        print(f"[{task['id']}/{total}] {task['tool']}")

        start_task(task)

        try:

            result = execute_tool(task)

            finish_task(task)

            results.append(
                {
                    "id": task["id"],
                    "tool": task["tool"],
                    "status": task["status"],
                    "started_at": task["started_at"],
                    "finished_at": task["finished_at"],
                    "duration": task["duration"],
                    "result": result,
                }
            )

        except Exception as e:

            fail_task(task)

            results.append(
                {
                    "id": task["id"],
                    "tool": task["tool"],
                    "status": task["status"],
                    "started_at": task["started_at"],
                    "finished_at": task["finished_at"],
                    "duration": task["duration"],
                    "result": str(e),
                }
            )

    return results
