from core.ai import ask_ai
from core.planner import plan_task
from core.registry import execute_tool

messages = [
    {
        "role": "system",
        "content": "You are MyAgent running inside Termux."
    }
]

print("=" * 40)
print("      MyAgent V7.2")
print("=" * 40)
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    tasks = plan_task(user)

    if tasks:
        for task in tasks:
            result = execute_tool(task)
            print(result)
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
