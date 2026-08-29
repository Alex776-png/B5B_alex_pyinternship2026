from pathlib import Path

relative_path = input("Enter a relative file path: ")

file_path = Path(relative_path)

print("Absolute path:", file_path.resolve())