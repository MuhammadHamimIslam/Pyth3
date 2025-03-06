"""
set doesn't allow unhashable type: 'list', 'dict'
The items in a set are unordered, unchangeable 
set doesn't allow duplicates 

"""
set1 = {"Python", 1991, True}
print("set1: ", set1)

set2 = {4, 3, 5, 2, 4, 9}
print("set2: ", set2)

"adding item to set"

set1.add("Python is easy")
print("set1: ", set1)

set3 = {11, 13, 15, 17}
set2.update(set3) # concating 2 iterable
print("set2: ", set2)

set1.update([])

"removing item from set"
set2.remove(9)
print("set2: ", set2)

