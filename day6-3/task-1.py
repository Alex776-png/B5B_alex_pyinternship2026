from pathlib import Path

backup_folder = Path("backup")

if not backup_folder.exists():
    backup_folder.mkdir()
    print("Created backup folder.")
else:
    print("backup folder already exists.")
