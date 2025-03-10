list1 = [9, 3, 5, 2, 1, 6, 9, 7, 4]
list2 = ["o", "l", "f", "h", "x", "t", "g",]
list3 = ["Orange", "apple", "banana", "Jackfruit", "Mango"]

"Using list.sort(key = None, reverse=False)"

list1.sort() # sorts list as numeric order
print(f"list1: {list1}")

list2.sort() # sorts list as alphabetical order 
print(f"list2: {list2}")

list1.sort(reverse = True) # reverseslist as numeric order 
print(f"list1: {list1}")

list2.sort(reverse = True) # reverses list as alphabetical order 
print(f"list2: {list2}")

list3.sort() # as sorting is case sensitive this causes problems
print(f"list3: {list3}")

list3.sort(key = str.lower) # now sorts correctly 
print(f"list3: {list3}")

list1.reverse() # reverses the list
print(f"list2: {list2}")

def sort(elm):
  return abs(elm - 50)
list1.sort(key = sort) # using custom function to sort list
print(f"list1: {list1}")


"Using sorted(iterable, key = None, reverse = False)"
list4 = sorted(list1)
print(f"list4: {list4}")
