import heapq

myArray = [0, 9, 6, 12, 3, 99, 3, 67, 23, 45]

"""heapq.nlargest(num, collection, key)
num -> the numbers of items that we want to receive 
collection -> the list
key -> function 
"""

print(heapq.nlargest(6, myArray))

"heapq.nlargest(num, list, key)"

print(heapq.nsmallest(6, myArray))

"heapq.heapify(collection)"

heapq.heapify(myArray) # transforms list into heap object 
print(myArray)
"heap.heappush(collection, item)"

heapq.heappush(myArray, 34)
print(myArray)

"heapq.heappop(collection)"

heapq.heappop(myArray) # removes the first smallest item from the list 
print(myArray)

"heapq.heapreplace(heap, item)"

heapq.heapreplace(myArray, 48) # Pop and return the current smallest value, and add the new item.
print(myArray)
