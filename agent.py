import os
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
MODEL = os.getenv("MODEL")


def run_local_task(prompt):
    text = prompt.lower().strip()

    if text == "list files":
        return subprocess.getoutput("ls")

    elif text == "show current directory":
        return subprocess.getoutput("pwd")

    elif text.startswith("make folder "):
        folder = prompt[12:].strip()
        subprocess.run(["mkdir", "-p", folder])
        return f"Folder '{folder}' created."

    elif text.startswith("create file "):
        filename = prompt[12:].strip()
        open(filename, "a").close()
        return f"File '{filename}' created."

    elif text.startswith("read file "):
        filename = prompt[10:].strip()
        try:
            with open(filename, "r") as f:
                return f.read()
        except Exception as e:
            return str(e)

    elif text.startswith("write "):
        try:
            parts = prompt[6:].split("=>", 1)
            filename = parts[0].strip()
            content = parts[1].strip()

            with open(filename, "w") as f:
                f.write(content)

            return f"Written to {filename}."

        except:
            return "Usage: write filename => text"

    elif text.startswith("append "):
        try:
            parts = prompt[7:].split("=>", 1)
            filename = parts[0].strip()
            content = parts[1].strip()

            with open(filename, "a") as f:
                f.write("\n" + content)

            return f"Added to {filename}."

        except:
            return "Usage: append filename => text"

    elif text.startswith("delete file "):
        filename = prompt[12:].strip()

        try:
            os.remove(filename)
            return f"{filename} deleted."

        except Exception as e:
            return str(e)

    elif text.startswith("delete folder "):
        folder = prompt[14:].strip()

        try:
            os.rmdir(folder)
            return f"{folder} deleted."

        except Exception as e:
            return str(e)

    elif text.startswith("find "):
        name = prompt[5:].strip()
        return subprocess.getoutput(f"find . -iname '*{name}*'")

    elif text.startswith("run "):

        command = prompt[4:].strip()

        allowed = [
            "pwd",
            "ls",
            "whoami",
            "date",
            "df -h",
            "free -h"
        ]

        if command not in allowed:
            return "Command not allowed."

        return subprocess.getoutput(command)

    return None


print("===================================")
print("        MyAgent V5")
print("===================================")
print("Local Tools + OpenRouter AI")
print("Type 'exit' to quit.\n")

while True:

    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    task = run_local_task(prompt)

    if task is not None:
        print("\nMyAgent:", task)
        print()
        continue

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "MyAgent V5"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are MyAgent V5 running in Termux. "
                    "Help with Linux, Python, programming, automation, "
                    "and explain commands clearly."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code != 200:
            print("\nError:")
            print(response.text)
            continue

        result = response.json()

        print("\nAI:")
        print(result["choices"][0]["message"]["content"])
        print()

    except Exception as e:
        print("\nError:", e)
