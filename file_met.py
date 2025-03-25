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

"Creating a directory"
# using makedirs() function 
try:
    newDirectory = "new.txt" 
    os.makedirs(newDirectory) # makes a new directory 
    print(f"{newDirectory} created successfully!")
except Exception as e:
    print(e)

# using mkdir() function
try:
    os.mkdir("Test") # creates a new directory 
    print("Directory created successfully!")
except Exception as e:
    print(e)

"Getting the current working directory"
# using os.getcwd() we can get the current working directory 
currentWorkingDirectory = os.getcwd()
print(f"{currentWorkingDirectory = }")

"Listing Files and Directories"

directory = os.getcwd()
print(f"All files in the directory: {os.listdir(directory)}") # returns all directory and files in a directory as a list

"Changing the current working directory"

try:
    newDirectory = "/storage/2350-1CF0/Android/data/io.spck/files/py-proj"
    os.chdir(newDirectory) # changes the current working directory to the new directory 
    print("Directory changed successfully!")
except Exception as e:
    print(e)

"Removing an empty directory"

try:
    direct = os.getcwd()
    os.rmdir(direct) # removes the directory 
except Exception as e:
    print(e)

