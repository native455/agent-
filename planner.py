import re

def plan_task(user_input):
    text = user_input.lower()

    tasks = []

    # Website project
    if "website" in text:

        folder = "Website"

        m = re.search(
            r"called\s+([A-Za-z0-9_-]+)|named\s+([A-Za-z0-9_-]+)",
            user_input,
            re.IGNORECASE,
        )

        if m:
            folder = next(g for g in m.groups() if g)

        tasks.append({
            "tool":"create_folder",
            "args":[folder]
        })

        tasks.append({
            "tool":"create_file",
            "args":[f"{folder}/index.html"]
        })

        tasks.append({
            "tool":"create_file",
            "args":[f"{folder}/style.css"]
        })

        tasks.append({
            "tool":"create_file",
            "args":[f"{folder}/script.js"]
        })

        return tasks

    # Single folder

    if "folder" in text:

        m = re.search(
            r"folder\s+(?:called|named)?\s*([A-Za-z0-9_-]+)",
            user_input,
            re.IGNORECASE,
        )

        if m:
            return [{
                "tool":"create_folder",
                "args":[m.group(1)]
            }]

    if text.startswith("read "):
        return [{
            "tool":"read_file",
            "args":[user_input[5:].strip()]
        }]

    if "list files" in text:
        return [{
            "tool":"list_files",
            "args":[]
        }]

    return None
