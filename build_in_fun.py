from functools import reduce # reduce is inside the module 

# there're several build in function in python

my_list = [1, 3, 4, 2, 5, 6, 2, 4, 9, 7]

# map(key, item)

print(list(map(lambda x: x + 2, my_list))) # apply key function to all elements in the item

# filter(key, item)

print(list(filter(lambda x: x % 2 == 0, my_list))) # filters from the elements in the item 

# reduce(accumulator, current)

print(reduce(lambda x, y: x + y, my_list)) # reduces the item's elements to one value

# all(iterable)

if all(i % 2 == 0 for i in my_list): # checks if all numbers are even
    print("All are even!")
else:
    print("All aren't even")
    
# any(iterable)

if any(i % 2 == 0 for i in my_list): # checks if any number is even
    print("some number(s) are even!")
else:
    print("No number is even")

# max(iterable)
print(max(my_list)) # returns the maximum number 

# min(iterable)
print(min(my_list)) # returns the minimum number 

# chr(int) 
print(chr(1000)) # integer to unicode character 

# ord(character) 
print(ord("❤")) #  unicode to integer