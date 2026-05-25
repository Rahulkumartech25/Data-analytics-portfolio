import os
import shutil

# Folder path you want to organize
base_path = os.getcwd()  # You can change this to any path you want

# File type mapping
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.sh', '.bat'],
}

# Create top-level folders for each category
for folder in file_types.keys():
    category_dir = os.path.join(base_path, folder)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

# organize files
for item in os.listdir(base_path):
    file_path = os.path.join(base_path, item)

    # skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    file_ext = os.path.splitext(item)[1].lower()

    for folder, extensions in file_types.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(base_path, folder, item))
           

print("Files organized successfully✅")