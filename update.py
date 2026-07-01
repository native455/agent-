import os
import shutil
from datetime import datetime

BACKUP_DIR = "backups"


def ensure_backup_dir():
    os.makedirs(BACKUP_DIR, exist_ok=True)


def backup_file(filename):
    if not os.path.exists(filename):
        return False

    ensure_backup_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(filename)}_{timestamp}.bak"

    shutil.copy2(
        filename,
        os.path.join(BACKUP_DIR, backup_name)
    )

    return backup_name


def write_file(filename, content):
    folder = os.path.dirname(filename)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def update_file(filename, content):
    backup = backup_file(filename)

    write_file(filename, content)

    if backup:
        return f"Updated {filename}\nBackup: backups/{backup}"

    return f"Created {filename}"


def list_backups():
    ensure_backup_dir()

    return sorted(os.listdir(BACKUP_DIR))


if __name__ == "__main__":

    print("=" * 40)
    print(" MyAgent Update Utility")
    print("=" * 40)

    while True:

        print("\n1. List backups")
        print("2. Exit")

        choice = input("> ")

        if choice == "1":

            backups = list_backups()

            if not backups:
                print("No backups found.")
            else:
                for b in backups:
                    print("-", b)

        elif choice == "2":
            break
