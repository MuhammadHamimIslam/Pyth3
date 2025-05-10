from collections import Counter 

list1 = [6, 4, 8, 6, 5, 7, 2, 4, 3, 5, 5, 1, 6, 9, 4, 7, 1]

count = Counter(list1) # returns the counter 

print(dict(count)) # prints how many times items are present

print(list(count.elements())) # returns all of the elements

print(count.most_common()) # returns the tuple form of element, element count

print(count.total()) # computes the sum of the counts

