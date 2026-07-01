import os
import shutil
import subprocess

def list_files(path="."):
    return os.listdir(path)

def create_folder(name):
    os.makedirs(name, exist_ok=True)
    return f"Folder '{name}' created."

def create_file(filename):
    with open(filename, "w") as f:
        pass
    return f"File '{filename}' created."

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return "File saved."

def append_file(filename, content):
    with open(filename, "a") as f:
        f.write(content)
    return "Content appended."

def delete_file(filename):
    os.remove(filename)
    return "File deleted."

def copy_file(src, dst):
    shutil.copy(src, dst)
    return "File copied."

def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout if result.stdout else result.stderr
