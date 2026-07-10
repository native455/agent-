"""
MyAgent Code Generator

Version: 13.3.0
"""

from core.project_templates import (
    create_flask,
    create_python_cli,
)


class CodeGenerator:

    def generate(self, project_type, project_name):

        project_type = project_type.lower()

        if project_type == "flask":
            location = create_flask(project_name)

        elif project_type == "python":
            location = create_python_cli(project_name)

        else:
            return {
                "success": False,
                "error": f"Unknown project type: {project_type}"
            }

        return {
            "success": True,
            "project": project_name,
            "type": project_type,
            "location": location,
        }


generator = CodeGenerator()
