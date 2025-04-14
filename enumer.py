from enum import Enum, unique # Enum for Enum class and unique for @unique decorator 
"Enumeration is the process of assigning fixed constant values to a set of strings so that each string can be identified by the value bound to it"


"we can use @unique decorator to set unique value"

@unique
class mathConst(Enum): # a class where Enum is the parent class 
    # all values should be unique
    PI = 3.1416
    e = 2.71828
    PHI = 1.61803

piObj = mathConst.PI

print(piObj) # returns the object 
print(piObj.name) # returns the name
print(piObj.value) # returns the value 

"Enum also can be created using constructor Enum('className', 'Value1 Value2 Value3')"
# this automatically assigns 1, 2, 3 serially
numbers = Enum("numbers", "num1 num2 num3")

print(numbers.num2.value)

# to set manually value, we can use list and tuple 
physicsConst = Enum("physicsConst",[
    ("LightSpeed", 3e8),
    ("PlankConst", 6.626e-34),
    ("BoltmanConst", 1.38e-23)
])

print(physicsConst.LightSpeed.value)


"Iterating through Enum"

for constant in mathConst: # for loop
    print(f"{constant.name}: {constant.value}")