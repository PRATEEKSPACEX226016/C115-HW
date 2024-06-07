import os

# Create Source file path
source = 'main.txt'

# Create a Destination file path
destination = 'newfile.txt'

# Check if the destination file already exists and remove it
if os.path.exists(destination):
    os.remove(destination)

# Use os.rename() to rename (move) the existing file
os.rename(source, destination)

print(f"File '{source}' has been renamed to '{destination}'")
