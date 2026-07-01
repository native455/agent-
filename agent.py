from core.ai import ask_ai
from core.router import decide
from core.executor import execute_plan

messages = [
    {
        "role": "system",
        "content": "You are MyAgent running inside Termux."
    }
]

print("=" * 45)
print("           MyAgent V7")
print("=" * 45)
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    tasks = decide(user)

    if tasks:

        print("\nExecuting plan...\n")

        results = execute_plan(tasks)

        for result in results:
            print(result)

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
