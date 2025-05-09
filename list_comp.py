list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = []
list3 = []
list4 = []
list5 = ["a", "b", "c", "d", "e"]
list6 = []
list7 = []
list8 = []

# adding item to a list based on condition 
for i in list1:
  if i % 2 == 1 :
    list2.append(i)
    
print(f"list2: {list2}")

# shorter approach 
# [ expression for var in iterable if condition ]
list3 = [i for i in list1 if i % 2 == 1]
print(f"list3: {list4}")

list4 = [i for i in range(1, 11) if i % 2 == 1]
print(f"list4: {list4}")

list6 = [i.upper() for i in list5 ]
print(f"list6: {list6}")

#using lambda function 
list7 = [(lambda x: x * 2) (x) for x in list3]
print(f"list7: {list7}")

list8 = [(x, y) for x in list3 for y in list5] # combination of list3 with list5
print(f"list8: {list8}")
