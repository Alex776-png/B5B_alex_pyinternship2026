import os
import shutil

base_dir = "organized_dir"

text_dir = os.path.join(base_dir, "TextFiles")
image_dir = os.path.join(base_dir, "ImageFiles")

# Create destination folders
os.makedirs(text_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)

# Move files into their respective folders
for filename in os.listdir(base_dir):
    source = os.path.join(base_dir, filename)

    # Skip directories
    if os.path.isdir(source):
        continue

    if filename.lower().endswith(".txt"):
        shutil.move(source, os.path.join(text_dir, filename))

    elif filename.lower().endswith(".png"):
        shutil.move(source, os.path.join(image_dir, filename))

print("Files organized successfully.")
