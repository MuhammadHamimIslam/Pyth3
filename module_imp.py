import module_exp # this will load all functions, class in this module 
"""
to load specific function or class:
from module_exp import avg,info
to load all functions or class
from module_exp import *
"""

print(module_exp.avg(1, 3, 5, 7, 9)) # prints the avg function in the module_exp file
print(module_exp.info(name = "abc", age = 26, email = "abc123@gmail.com"))