import os
import shutil
from datetime import datetime

BACKUP_DIR = "backups"


def backup_file(path):
    if not os.path.exists(path):
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.basename(path)

    shutil.copy2(
        path,
        os.path.join(
            BACKUP_DIR,
            f"{timestamp}_{filename}"
        )
    )


def write_file(path, content):
    backup_file(path)

    folder = os.path.dirname(path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {path}")


UPDATES = {

    "v10": [

    ]

}


def install(version):

    if version not in UPDATES:
        print("Unknown version.")
        return

    print(f"Installing {version}...")

    for update in UPDATES[version]:

        write_file(
            update["path"],
            update["content"]
        )

    print("Done.")


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage:")
        print("python update.py v10")
        exit()

    install(sys.argv[1])
