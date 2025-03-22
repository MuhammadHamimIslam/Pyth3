"To get a file, we have to use open() function"

# -> open(fileName, mode)
txtFile = open("example1.txt", "r")

print(txtFile.name) # prints the name of the file
print(txtFile.closed) # returns true if file is closed 
print(txtFile.mode) # gives the mode

"reading from file"
"To write to a file, we need to open with 'r' mode "

# using read() function -> str
with open("example1.txt", "r") as textFile: 
    content = textFile.read() # returns all content 
    print(content) # returns the whole content as a string 

# using readline() function (reads one line at once) -> str
with open('example1.txt', "r") as file:
    line = file.readline() # returns one line
    print(line) # prints the first line
    while line:
        print(line, end = "")
        line = file.readline()
    
# using readlines() function -> list 
with open('example1.txt', "r") as f1:
    cont = f1.readlines() # returns a list
    print(cont)

"closing a file "
# using close () function.

fl = open('example1.txt', "r")
fl.close() # closes the file 
print("file closed!")
"By using with keyword, The file will be automatically closed"

"writing to a file"
"If we open a file using 'w' open mode, The exiting content of the file will be removed"
# writing a file with "w" mode
"file writing with error handling"

# using "a" mode
"If we open a file using 'a' open mode, The content will be added after the previous content"

# -> using file.write()
try:
    with open("example2.txt", "w") as fl: 
        fl.write("Hello, World!")
        print("content added successfully!")
except PermissionError as e:
    print(e)

try:
    with open("example1.txt", "a") as file: 
        file.write("\n\nThis content will be added after the previous content")
except PermissionError:
    print("Permission Error!")


# -> using file.writelines()
lines = ["first line\n", "second line\n", "third line\n"]
try:
    with open("example2.txt", "w") as myFile:
        # readlines() takes a list of string and writes to the file
        myFile.readlines(lines)
        print("content added successfully")
except PermissionError as e:
    print(e)
    