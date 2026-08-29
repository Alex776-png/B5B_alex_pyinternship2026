import os
import shutil
import zipfile

zip_file = "organized_backup.zip"
directory = "organized_dir"

# Verify that the ZIP exists
if not os.path.isfile(zip_file):
    raise FileNotFoundError(f"{zip_file} was not found.")

# Verify that the ZIP is valid and not corrupted
with zipfile.ZipFile(zip_file, "r") as zip_ref:
    if zip_ref.testzip() is not None:
        raise RuntimeError("ZIP verification failed. The backup may be corrupted.")

print("ZIP backup verified successfully.")

# Delete the original directory and everything inside it
if os.path.exists(directory):
    shutil.rmtree(directory)
    print(f"Deleted: {directory}")
else:
    print(f"{directory} does not exist.")
