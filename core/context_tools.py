"""
MyAgent Context Tools

Version: 13.1.0
"""

from core.context_manager import context_manager


def show_context():
    """
    Return the current working context.
    """
    return context_manager.get()


def set_project_context(project):
    return context_manager.set_project(project)


def set_folder_context(folder):
    return context_manager.set_folder(folder)


def set_file_context(filename):
    return context_manager.set_file(filename)


def set_mode(mode):
    return context_manager.set_mode(mode)


def clear_context():
    return context_manager.clear()
