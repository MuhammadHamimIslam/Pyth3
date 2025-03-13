import random
"A function to find all unique numbers in a list"

def isUnique1(inputList): # using list loop
  result = []
  for i in inputList: 
    if i not in result: # check if item is in result 
      result.append(i)
  return result
def isUnique2(inputList): 
  return list(set(inputList)) # convert to set then again convert to list
  
"A function to find sum of all numbers in a list(using loop)"  
def sumOfList(inputList): 
  sum = 0
  for i in inputList: 
    sum += i
  return sum
 
"A function to create a list of 5 random integers"

def randomList():
  result = []
  for i in range(5): 
    result.append(random.randint(0, 100))
  return result 
  
