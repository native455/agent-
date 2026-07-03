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

from core.retry import retry

from core.plan_history import record_plan


def execute_plan(plan, goal="Unknown Task"):

    results = []

    total = len(plan)

    for task in plan:

        print(f"[{task['id']}/{total}] {task['tool']}")

        start_task(task)

        success, result, attempts = retry(
            execute_tool,
            task
        )

        if success:
            finish_task(task)
        else:
            fail_task(task)

        results.append(
            {
                "id": task["id"],
                "tool": task["tool"],
                "status": task["status"],
                "started_at": task["started_at"],
                "finished_at": task["finished_at"],
                "duration": task["duration"],
                "attempts": attempts,
                "result": result,
            }
        )

    # Save completed plan
    record_plan(goal, results)

    return results
