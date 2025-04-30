# there're several build in function in python

myList = [1, 3, 4, 2, 5, 6, 2, 4, 9, 7]

"map(key, item)"

print(list(map(lambda x: x + 2, myList))) # apply key function to all elements in the item

"filter(key, item)"

print(list(filter(lambda x: x % 2 == 0, myList))) # filters from the elements in the item 

"reduce(key, item)"

#print(reduce(lambda x, y: x * y, myList)) # reduces the item's elements to one value
