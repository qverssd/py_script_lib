import os
import shutil
import datetime

def create_backup(sources, destination):
    for path in sources:
        if not os.path.exists(path):
            print(f"Error: Path '{path}' does not exist.")
            return
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(destination, backup_name)

    print(f"Creating backup archive at {backup_path}")

if __name__ == "__main__":
    sources = [
        "example_folder",
        "example_file.txt"
    ]
    destination = "backups"

    if not os.path.exists(destination):
        os.makedirs(destination)

    create_backup(sources, destination)