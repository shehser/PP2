import os
import glob

# 1. Create nested directories
# The exist_ok=True argument prevents an error if the directory already exists
os.makedirs("project_root/src/data/raw", exist_ok=True)

# Create dummy files for demonstration purposes
with open("project_root/config.txt", "w") as f:
    f.write("config content")
with open("project_root/src/data/raw/dataset.txt", "w") as f:
    f.write("data content")

# 2. List files and folders in the immediate directory
print("Listing immediate contents:")
for item in os.listdir("project_root"):
    print(item)

# 3. Find files by extension (recursive search using glob)
# The recursive=True argument allows ** to match directories recursively
print("\nFinding all .txt files:")
txt_files = glob.glob("project_root/**/*.txt", recursive=True)
for file_path in txt_files:
    print(file_path)
