from pathlib import Path

notes_file = Path("notes.txt")

if not notes_file.exists():
    notes_file.touch()
    print("Created notes.txt")

print("File size:", notes_file.stat().st_size, "bytes")
print("Suffix:", notes_file.suffix)