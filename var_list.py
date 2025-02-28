list1 = ["Python", 1990, {"isEasy": True}, [1, 2, 3, 4, 5] ]

list2 = [10, 20, 30, 40] 

print(list1)

print(list1[2]) # accessing element of list 
list1.append("Python is so easy") # adding element to list (at the last )
print(list1)

list1.pop() # removes the last element 
print(list1)

list1[3] = [7, 8, 9, 10] # changing elm in list
print(list1)

list1.insert(1, "Python is popular") # inserts an element at index "1"
print(list1)

list1.remove([7, 8, 9, 10]) # removes the element 
print(list1)

print(sum(list2)) # gives the sum of all elm

print(max(list2)) # returns the maximum num

print(min(list2)) # returns the minimum num
