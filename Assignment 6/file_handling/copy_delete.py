import os
import shutil

# Copy a file
shutil.copy("sample.txt", "sample_backup.txt")
print("File copied successfully.")

# Safely delete the backup
if os.path.exists("sample_backup.txt"):
    os.remove("sample_backup.txt")
    print("Backup deleted.")
