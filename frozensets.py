"""
Frozenset is an unchangeable  object which is
like a set but  unchangeable.
"""

"Frozenset is iterable"

frznset = frozenset(("mango", "orange", "banana", "guava"))

print("frozenset is: ", frznset)

"As frozenset is unchangeable the item isn't  accessible and unchangeable"

#print(frznset[0])  will raise an error 
"accessing items using for loop"
for i in frznset: 
  print(i)