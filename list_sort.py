list1 = [9, 3, 5, 2, 1, 6, 9, 7, 4]
list2 = ["o", "l", "f", "h", "x", "t", "g",]
list3 = ["Orange", "apple", "banana", "Jackfruit", "Mango"]

list1.sort() # sorts list as numeric order
print(list1)

list2.sort() # sorts list as alphabetical order 
print(list2)

list1.sort(reverse = True) # reverseslist as numeric order 
print(list1)

list2.sort(reverse = True) # reverses list as alphabetical order 
print(list2)

list3.sort() # as sorting is case sensitive this causes problems
print(list3)

list3.sort(key = str.lower) # now sorts correctly 
print(list3)

list1.reverse() # reverses the list
print(list2)

def sort(elm):
  return abs(elm - 50)

list1.sort(key = sort) # using custom function to sort list
print(list1)