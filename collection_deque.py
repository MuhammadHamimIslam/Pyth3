from collections import deque

"deque -> is an object like a list where appending, pop etc can be done fast"

dq1 = deque([1, 2, 3, 4, 5])
print(dq1)

dq1.append(10) # adds the item at the end of the deque
print(dq1)

dq1.appendleft(0) # adds the item at the left side (beginning )
print(dq1)

dq1.pop() # removes the last item 
print(dq1)

dq1.popleft() # removes the item from the left side (beginning )
print(dq1)

print(dq1.index(4)) # returns the index of the item

dq2 = deque([6, 7, 8])

dq2.extend(dq1) # add the deque at the end of the deque
print(dq2)

dq1.extendleft(dq2)# add the deque at the beginning of the deque
print(dq1)

dq1.insert(-1, 0) # adds the item in the index of 0
print(dq1)

print(dq1.count(5)) # returns how much of time the item is present in the deque

dq1.reverse() # reverses the order of the dequeprint()
print(dq1)

dq1.rotate(1) # rotates the deque
print(dq1)

dq2.clear() # clears all items in the deque
print(dq2)