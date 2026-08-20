
### step 1: Get the current folder
import os

current_folder = os.getcwd()       #getcwd() = Get Current Working Directory

print("Current folder:", current_folder)
print("="*70)

### step 2: List files and folders
import os

current_folder = os.getcwd()

print("Current folder:", current_folder)

print("\nFiles and folders:")
print(os.listdir())
print("="*70)

### step 3: Check file vs folder
import os

current_folder = os.getcwd()

items = os.listdir()

for item in items:
    if os.path.isfile(item):
        print(item,"File")
    elif os.path.isdir(item):
        print(item,"Folder")
print("="*70)

### step 4: Create a folder with python
import os

folder_name = "text_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully.")
else:
    print("Folder already exists.")
print("="*70)

###File extension checker
import os
items = os.listdir()

for item in items:
    if os.path.isfile(item):
        print(item)