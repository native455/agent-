import re

def plan_task(user_input):
    text = user_input.lower()

    # Create folder
    if "create" in text and "folder" in text:
        match = re.search(r"folder (called|named)?\s*([A-Za-z0-9_-]+)", user_input, re.IGNORECASE)

        if match:
            return {
                "tool": "create_folder",
                "args": [match.group(2)]
            }

    # Read file
    if text.startswith("read "):
        filename = user_input[5:].strip()

        return {
            "tool": "read_file",
            "args": [filename]
        }

    # List files
    if "list files" in text:
        return {
            "tool": "list_files",
            "args": []
        }

    return None
