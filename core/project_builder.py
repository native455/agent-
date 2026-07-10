"""
MyAgent Project Builder

Version: 13.3.0
"""

import os

from core.generator import generate_file
from core.code_generator import generator


class ProjectBuilder:
    """
    Build complete projects.
    """

    def build_website(self, project):

        os.makedirs(project, exist_ok=True)

        html = generate_file("html", project)
        css = generate_file("css", project)
        js = generate_file("javascript", project)

        with open(
            os.path.join(project, "index.html"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(html)

        with open(
            os.path.join(project, "style.css"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(css)

        with open(
            os.path.join(project, "script.js"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(js)

        return {
            "success": True,
            "message": f"Website '{project}' created successfully.",
            "location": os.path.abspath(project),
        }

    def build_project(self, project_type, project_name):
        """
        Build a project from a template.
        """

        return generator.generate(
            project_type,
            project_name,
        )


builder = ProjectBuilder()


# Backward compatibility
def build_website(project):
    return builder.build_website(project)


def build_project(project_type, project_name):
    return builder.build_project(
        project_type,
        project_name,
    )
