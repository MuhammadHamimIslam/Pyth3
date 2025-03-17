"A function to find unique numbers in a given tuple"

def findUnique (inp):
  result = []
  for i in inp: 
    if i not in result: 
      result.append(i)
  return tuple(result)

"A function to find sum of all numbers in a tuple"

def findSum(inp): 
  result = 0
  for i in inp: 
    result += i
  return result

"A function to create a tuple of 5 random integers"

def randTuple(): 
  import random
  result = []
  for _ in range(5):
    randomNum = random.randint(1, 100)
    result.append(randomNum)
  return tuple(result)

"A function to square all the elements in a tuple"

def squareTuple(inp): 
  result = [x ** 2 for x in inp]
  return tuple(result)
  
