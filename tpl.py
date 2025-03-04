myTpl = ("python", "1991", False, [11, 22]) # a simple tuple 

print(myTpl)

print(myTpl[3]) # getting item by index

print(myTpl[-1]) # getting item by negative index

print(myTpl[0:3]) # slicing just like list

print("python" in myTpl) # checks if item is present in tuple 

"Updating a tuple"

temp = list(myTpl)
temp[2] = True # changing element by creating a temporary list
myTpl = tuple(temp)
print(myTpl)

"Adding items to tuple"

x = list(myTpl)  # creating a temporary list
x.append("Python is easy")
myTpl = tuple(x)
print(myTpl)

y = ("Python was first released in 1991",)
myTpl += y # concating 2 tuples 
print(myTpl)

"removing item from tuple"

z = list(myTpl)
z.pop()
z.remove(myTpl[4]) # creating a temporary list 
myTpl = tuple(z)
print(myTpl)

"Deleting a tuple"

del myTpl 
# print(myTpl) "Tis will throw an error as myTpl is deleted"
admins = ("abc", "xyz", "mno", "pqr")

"Unpacking a tuple"

admin1, *others = admins
print(admin1) # returns admins[0]
print(others) # returns a list of other items

"looping to tuple"

for i in admins: # a for loop to a tuple 
  print("list item: ", i)

for i in range(len(admins)): # looping through index using for loop
  print(f"list item in index{i} is:{admins[i]}")
  
i = 0
while i < len(admins): # looping through index using while loop
  print(f"list item in index{i} is:{admins[i]}")
  i += 1

"joining  tuples" 

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8, 1, 2, 1, 1, 1)
myTuple = tuple1 + tuple2
print(myTuple)

"multiplying items of tuple"
double = myTuple * 2 # multiplying elements of a tuple 
print(double)

"tuple methods"

print(myTuple.count(1)) # returns how many times a item is present in a tuple 

print(myTuple.index(8)) # returns the index of the item