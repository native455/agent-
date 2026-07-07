"""
MyAgent Project Router

Version: 13.0.0

Routes project-related commands without AI.
"""

import re


def route_project(user):

    text = user.strip()

    # Create project <name>
    m = re.match(r"create project (.+)", text, re.IGNORECASE)
    if m:
        return [
            {
                "tool": "create_project",
                "args": [m.group(1).strip()]
            }
        ]

    # Open project <name>
    m = re.match(r"open project (.+)", text, re.IGNORECASE)
    if m:
        return [
            {
                "tool": "open_project",
                "args": [m.group(1).strip()]
            }
        ]

    # Close project
    if text.lower() == "close project":
        return [
            {
                "tool": "close_project",
                "args": []
            }
        ]

    # List projects
    if text.lower() == "list projects":
        return [
            {
                "tool": "list_projects",
                "args": []
            }
        ]

    # Project status
    if text.lower() == "project status":
        return [
            {
                "tool": "project_status",
                "args": []
            }
        ]

    # Add task <task>
    m = re.match(r"add task (.+)", text, re.IGNORECASE)
    if m:
        return [
            {
                "tool": "add_task",
                "args": [m.group(1).strip()]
            }
        ]

    # Show tasks
    if text.lower() == "show tasks":
        return [
            {
                "tool": "show_tasks",
                "args": []
            }
        ]

    # Complete task <number>
    m = re.match(r"complete task (\d+)", text, re.IGNORECASE)
    if m:
        return [
            {
                "tool": "complete_task",
                "args": [int(m.group(1))]
            }
        ]

    # Add note <text>
    m = re.match(r"add note (.+)", text, re.IGNORECASE)
    if m:
        return [
            {
                "tool": "add_note",
                "args": [m.group(1).strip()]
            }
        ]

    # Show notes
    if text.lower() == "show notes":
        return [
            {
                "tool": "show_notes",
                "args": []
            }
        ]

    return None
