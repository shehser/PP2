import os
import shutil

# Setup initial test folders and file
os.makedirs("source_folder", exist_ok=True)
os.makedirs("destination_folder", exist_ok=True)

with open("source_folder/report.pdf", "w") as f:
    f.write("pdf data")

# 1. Copy a file from one directory to another
# shutil.copy() copies the file data and destination can be a directory
shutil.copy("source_folder/report.pdf", "destination_folder")
print("File copied successfully.")

# 2. Move a file from one directory to another
# This removes the file from the source and places it in the destination
shutil.move("source_folder/report.pdf", "destination_folder/moved_report.pdf")
