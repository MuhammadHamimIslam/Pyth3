"try-except block"
try:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    print("The result is", num1 / num2)
  
except ValueError: # if user gives input a innumeric value(that causes ValueError), this except block will be executed else ignored
    print("Enter a numeric value!")
  
except ZeroDivisionError: # if the 2nd number is 0 (ZeroDivisionError), this except block will be executed 
    print("Can't divide by 0!")
# we can add else block too
else:
    print("No error occurred!")

"try except finally block"

try:
    with open('example2.txt', 'w') as f:
        f.write("Hello, World!")
except PermissionError as e:
    print("PermissionError! can't write to the file", e)
finally:
    print("File closed")

"raising an exception"
# syntax raise [Exception [, arg [, Traceback]
# Exception is the type of exception and argument is a value for the exception argument

gameLevel = int(input("Enter your level in the game: "))
if gameLevel < 1: 
    raise Exception("Invalid Level")

"Custom exception"
class customException(Exception): # a class that inherits from Exception class
    def __init__(self, msg):
        self.message = msg # set error msg 
        super().__init__(self.message) # get all properties 

error = False
if error == True: 
    raise customException("This is a custom Exception")
    
"re-raising exception"

def readFile(file): 
    try:
        with open(file) as f: 
            print(f.read())
    except FileNotFoundError as e:
        print(f"Can't find the file {file}")
        raise Exception from e

try:
    readFile("example.txt")
except FileNotFoundError as e:
    print("Raising error again")
    
    