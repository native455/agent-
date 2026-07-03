from core.ai import ask_ai
from core.router import decide
from core.executor import execute_plan

messages = [
    {
        "role": "system",
        "content": "You are MyAgent running inside Termux."
    }
]

print("=" * 50)
print("           MyAgent V11")
print("=" * 50)
print("Planner V2 Enabled")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ").strip()

    if user.lower() == "exit":
        break

    plan = decide(user)

    if len(plan) > 0:

        print("\n========== PLAN ==========")

        for step, task in enumerate(plan, start=1):
            print(
                f"{step}. {task['tool']} {task.get('args', [])}"
            )

        print("==========================\n")

        results = execute_plan(plan)

        print("\n========== RESULTS ==========")

        for item in results:
            icon = "✓"
            if item["status"] == "failed":
                icon = "✗"

            print(
                f"{icon} Step {item['id']} | "
                f"{item['tool']} | "
                f"Attempts: {item['attempts']} | "
                f"{item['duration']}s | "
                f"{item['result']}"
            )

        print()

        continue

    messages.append({
        "role": "user",
        "content": user
    })

    try:
        reply = ask_ai(messages)
        print("\nMyAgent:", reply, "\n")

        messages.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        print("AI Error:", e)
