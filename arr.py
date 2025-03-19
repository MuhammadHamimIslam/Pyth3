import array as arr

"As array isn't a built in data type in python.We need to import the 'array' module"
"""
array syntax:
    Array = arr.array("typecode", values)
    
'typecode' is used to define the data type of the array 

typecode --------------> data type 
'b', 'h', 'i', 'l', 'q'  signed int
'B', 'H', 'I', 'L', 'Q'  unsigned int
'u'                      unicode char
'f', 'd'                 floating num

and value can be list, tuple, dictionary 
"""
# an array with int type
intArr = arr.array("b", [1, 2, 3, 4, 5])
print(f"integer type array: {intArr}\n type: {type(intArr)}\n")

charArr = arr.array("u", "Hello, World!")
print(f"character type array: {charArr}\n type: {type(intArr)}\n")

decArr = arr.array("f", (1.1, 2.2, 3.33))
print(f"decimal type array: {decArr}\n type: {type(intArr)}\n")
