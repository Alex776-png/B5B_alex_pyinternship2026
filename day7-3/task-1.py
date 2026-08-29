import shutil
from pathlib import Path

source = Path("important.txt")
backup = Path("important_backup.txt")

if source.exists():
    shutil.copy2(source, backup)
    print("Backup created:", backup)
else:
    print("Error: important.txt not found.")
