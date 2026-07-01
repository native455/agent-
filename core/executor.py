from core.registry import execute_tool

def execute_plan(tasks):
    results = []

    for task in tasks:
        try:
            result = execute_tool(task)
            results.append(result)
        except Exception as e:
            results.append(f"Tool Error: {e}")

    return results
