from ai import ask_ai
from tools import (
    create_folder,
    read_file,
    list_files,
)

messages = [
    {
        "role": "system",
        "content": (
            "You are MyAgent running in Termux. "
            "If the user wants to chat, answer normally."
        )
    }
]

print("=" * 40)
print("      MyAgent V6.4")
print("=" * 40)
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    # Local commands
    if user.lower().startswith("create folder "):
        name = user[14:].strip()
        print(create_folder(name))
        continue

    if user.lower().startswith("read "):
        filename = user[5:].strip()
        try:
            print(read_file(filename))
        except Exception as e:
            print(e)
        continue

    if user.lower() == "list files":
        print(list_files())
        continue

    # AI chat
    messages.append({"role": "user", "content": user})

    try:
        reply = ask_ai(messages)
        print("\nMyAgent:", reply, "\n")
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print("Error:", e)
