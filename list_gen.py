myList1 = ["Apple", "Banana", "Berry", "Mango"]
myList2 = ["Jackfruit", "Orange", "Date", "Guava"]

" copying list "
newList1 = myList1.copy() # copy the item of list using list.copy()
print(newList1)

newList2 = list(myList1) # copy the item of list using list() constructor 
print(newList2)

newList3 = myList1[:] # copy the item of list using slice 
print(newList3)

" joining list "

newList4 = myList1 + myList2 # joins 2 lists using "+" operator 
print(newList4)

newList5 = myList1
newList5.extend(myList2) # joins 2 lists using list1.extend(list2)
print(newList5)
