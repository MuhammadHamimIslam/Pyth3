list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = []
list3 = []
list4 = []
list5 = ["a", "b", "c", "d", "e"]
list6 = []
# adding item to a list based on condition 
for i in list1:
  if i % 2 == 1 :
    list2.append(i)
    
print(list2)

# shorter approach 
# [ expression for var in iterable if condition ]
list3 = [i for i in list1 if i % 2 == 1]
print(list3)

list4 = [i for i in range(1, 11) if i % 2 == 1]
print(list4)

list6 = [i.upper() for i in list5 ]
print(list6)

