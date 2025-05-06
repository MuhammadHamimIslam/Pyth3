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

