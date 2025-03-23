import os

"Renaming a file"
# to rename a file we need to import os

oldName = "example2.txt"
newName = "python_test.txt"

try:
    os.rename(oldName , newName) # will rename the file 
    print("Rename successfully!")
except Exception as e:
    print(f"Error occured! : {e}")

"Deleting a file"

try:
    os.remove(oldName) # delete the file
    print("File deletion successful!")
except Exception as e:
    print(f"Error occured: {e}")

"Checking if a directory exists"

print(os.path.exists(oldName)) # returns true if this file/folder exists
