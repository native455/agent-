from core.ai import ask_ai


def generate_file(filetype, project_name):

    prompts = {
        "html": f"""
Create a complete HTML5 homepage for a project called '{project_name}'.

Return ONLY HTML.
""",

        "css": f"""
Create modern responsive CSS for '{project_name}'.

Return ONLY CSS.
""",

        "javascript": f"""
Create JavaScript for '{project_name}'.

Return ONLY JavaScript.
"""
    }

    messages = [
        {
            "role": "system",
            "content": "You are an expert software engineer. Return code only."
        },
        {
            "role": "user",
            "content": prompts[filetype]
        }
    ]

    return ask_ai(messages)
