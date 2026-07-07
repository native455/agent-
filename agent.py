"""
MyAgent

Version: 12.4.3
"""

from core.bootstrap import bootstrap

# Initialize MyAgent
bootstrap()

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
print("            MyAgent V12.4.3")
print("=" * 50)
print("Intent Router Enabled")
print("Capability Registry Enabled")
print("Bootstrap Enabled")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ").strip()

    if user.lower() == "exit":
        print("\nGoodbye.\n")
        break

    plan = decide(user)

    if isinstance(plan, list) and len(plan) > 0:

        print("\n========== PLAN ==========\n")

        for step, task in enumerate(plan, start=1):
            print(
                f"{step}. {task.get('tool')} {task.get('args', [])}"
            )

        print("\n==========================")

        results = execute_plan(
            plan,
            goal=user
        )

        print("\n========== RESULTS ==========\n")

        for item in results:

            icon = "✓"

            if item["status"] == "failed":
                icon = "✗"

            print(
                f"{icon} Step {item['id']} | "
                f"{item['tool']} | "
                f"{item['status']} | "
                f"Attempts: {item['attempts']} | "
                f"{item['duration']:.2f}s | "
                f"{item['result']}"
            )

        print()

        continue

    messages.append(
        {
            "role": "user",
            "content": user,
        }
    )

    try:

        reply = ask_ai(messages)

        if reply is None:
            reply = "I don't have a response."

        print(f"\nMyAgent: {reply}\n")

        messages.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )

    except Exception as e:

        print(f"\nAI Error: {e}\n")
