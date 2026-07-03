from core.registry import execute_tool


def execute_plan(plan):

    results = []

    total = len(plan)

    for task in plan:

        print(
            f"[{task['id']}/{total}] {task['tool']}"
        )

        task["status"] = "running"

        try:

            result = execute_tool(task)

            task["status"] = "completed"

            results.append({
                "id": task["id"],
                "tool": task["tool"],
                "status": task["status"],
                "result": result
            })

        except Exception as e:

            task["status"] = "failed"

            results.append({
                "id": task["id"],
                "tool": task["tool"],
                "status": task["status"],
                "result": str(e)
            })

    return results
