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

set1.update(["python was first released in 1991"])
print("set1: ", set1)

"removing item from set"

set2.remove(9) # removes an element
print("set2: ", set2)

set2.discard(15) # removes an element 
print("set2: ", set2)

set2.pop() # as set is unordered, we actually don't know which item will be removed 
print("set2: ", set2)

set3.clear() # clears all the items in a set
print("set3: ", set3)

del set3 # deletes a set completely 
# print(set3) will raise an error 

"looping through a set"

for i in set1: 
  print(i) # prints all items

"joining sets"
set4 = {4, 3, 6, 7, 1, 9}
set5 = {3, 9, 5, 6, 2,.4}

set3 = set4.union(set4) # preforms set union 
print(f"set3: ", set3)

set4.intersection_update(set5) # performs set intersection in the set4
print(f"set4: ", set4)

set6 = set5.intersection(set4) # performs set intersection in a new set
print(f"set6: ", set6)

set7 = {"apple", "cherry", "mango"}
set8 = {"banana", "apple", "berry"}

set7.symmetric_difference_update(set8) # adds this elements in set7 that're not in both set 
print(f"set7: ", set7)

set9 = set7.symmetric_difference(set8) # adds this elements in set7 that're not in both set in a new set
print(f"set9: ", set9)

print(set4.issubset(set3)) # returns true if set4 is a subset of set3

