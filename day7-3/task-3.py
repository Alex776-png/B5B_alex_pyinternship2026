import shutil

shutil.make_archive(
    "organized_backup",
    "zip",
    root_dir=".",
    base_dir="organized_dir"
)

print("ZIP backup created: organized_backup.zip")
