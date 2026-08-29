from pathlib import Path

current_folder = Path.cwd()

for file in current_folder.iterdir():
    if file.is_file() and file.suffix == ".py":
        print(file.name)
