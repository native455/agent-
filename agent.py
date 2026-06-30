from ai import ask_ai
from planner import plan_task
from tools import create_folder, read_file, list_files

messages = [
    {
        "role": "system",
        "content": "You are MyAgent running inside Termux."
    }
]

print("=" * 40)
print("      MyAgent V6.6")
print("=" * 40)
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    task = plan_task(user)

    if task:

        tool = task["tool"]
        args = task["args"]

        try:

            if tool == "create_folder":
                print(create_folder(*args))

            elif tool == "read_file":
                print(read_file(*args))

            elif tool == "list_files":
                print(list_files())

        except Exception as e:
            print("Tool Error:", e)

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
