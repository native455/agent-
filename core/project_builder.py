import os

from core.generator import generate_file


def build_website(project):

    os.makedirs(project, exist_ok=True)

    html = generate_file("html", project)
    css = generate_file("css", project)
    js = generate_file("javascript", project)

    with open(f"{project}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    with open(f"{project}/style.css", "w", encoding="utf-8") as f:
        f.write(css)

    with open(f"{project}/script.js", "w", encoding="utf-8") as f:
        f.write(js)

    return f"Website '{project}' created successfully."
