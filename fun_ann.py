"""
function annotation is a process to add meta data to a function.

syntax:
def fname(arg: argumentType) -> returnType:
  return ...
"""

def add(num1: int, num2: int) -> int:
  return num1 + num2
print(add(20, 20))


def message(name: str, meritStatus: str, **marks: str) -> str: 
  return f"Hey {name}! You {meritStatus} in your last exam. Here's your marks: \n Math: {marks['math']}, physics: {marks['physics']}"
msg = message("xyz", "passed", math = 90, physics = 87)  
print(msg)
# to see the annotations 

print(message.__annotations__)

"Decorator"
# decorator is a way to add extra information to a function without modifying the original function 

# decorator function 
def myDecorator(func): 
    def wrapper ():
        print("It's called at first!")
        # call the decorator 
        func()
        print("It's called at last!")
    return wrapper
    
@myDecorator
# the function that we want to decorate 
def sayHello():
    print("Hello everyone, What's up?")

# call the decorator 
sayHello()