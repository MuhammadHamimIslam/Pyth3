import copy

myList1 = ["Apple", "Banana", "Berry", "Mango"]
myList2 = ["Jackfruit", "Orange", "Date", "Guava"]
myList3 = [1, 2, 3, [4, 6]]

" copying list "
newList1 = myList1.copy() # copy the item of list using list.copy()
print(f"newList1: {newList1}")

newList2 = list(myList1) # copy the item of list using list() constructor 
print(f"newList2: {newList2}")

newList3 = myList1[:] # copy the item of list using slice 
print(f"newList3: {newList3}")

" joining list "

newList4 = myList1 + myList2 # joins 2 lists using "+" operator 
print(f"newList4: {newList4}")

newList5 = myList1
newList5.extend(myList2) # joins 2 lists using list1.extend(list2)
print(f"newList5: {newList5}")



"copying list with copy module"
# copy.copy() creates a shallow copy that's mean if changes are made to copied list the main list will also be changed 
copyList1 = copy.copy(myList3)
print(f"copyList1: {copyList1}")

copyList1[3][1] = 5
print(f"copyList: {copyList1}")
print(f"original list: {myList3}")

#copy.deepcopy() copies a list only with the reference of the original list
copyList2 = copy.deepcopy(myList3)
print(f"copyList2: ", copyList2)
