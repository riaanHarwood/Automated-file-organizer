from pathlib import Path
import shutil
import logging

# Target folder
# Note: Change this to the folder you want to organize on your machine. 
# Remove "automation" if you want to organize the entire Desktop or another directory. 

SOURCE_DIR = Path.home() / "Desktop" / "automation"


# Define file types and their corresponding folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".tar", ".gz"]
}

def organize_files():
    for file in SOURCE_DIR.iterdir():
        if file.is_file():
            for folder, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    target_dir = SOURCE_DIR / folder
                    target_dir.mkdir(exist_ok=True)

                    shutil.move(str(file), str(target_dir / file.name))
                    print(f"Moved {file.name} → {folder}")

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


if __name__ == "__main__":
    organize_files()