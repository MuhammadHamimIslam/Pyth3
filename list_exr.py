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
  import random 
  result = []
  for i in range(5): 
    result.append(random.randint(0, 100))
  return result 
  
"A function to create an list of the factorial of the input number"

def factorialList (inpNum: int) -> list: 
  result = []
  def factorial(n): 
    if n == 0: 
      return 1
    return n * factorial(n - 1)
  for i in range(0, inpNum): 
    result.append(factorial(i))
  return result 

"A function to filter the odd numbers in a list"

def filterOdd(inputList): 
  result = [i for i in inputList if i % 2 == 0] # use list compression to filter odds
  return result 

"A function to sort a list of dictionaries of users for their age"

def sortByAge(users): 
    users.sort(key = lambda a: a["age"]) # sort the list by user's age
    return users
  
"A function to flatten a list of lists"

def flattenList(inputList): 
  result = [] # an empty list
  for elm in inputList: # loop 
    if type(elm) == list: # elm is list add this to result 
      result.extend(flattenList(elm))
    else:
      result.append(elm) # else add to result
  return result

  print(flattenList([1, 2, 3, [4, 5, [6, 7]]]))

"A function to do union in multiple lists"

def union(*lists): 
  result = []
  for elm in lists:
    for item in elm: 
      if item not in result: 
        result.append(item)
  return result

"A function to find common elements in multiple lists"

def findCommon(*lists): 
  # convert the first element to set
  result = set(lists[0])
  for elm in lists[1:]: # loop through other elements 
    result &= set(elm) # convert others to set and do intersection 
  return list(result)

"A function to find Fibonacci sequence upto n"

def fibonacciSeq(n):
    result = [0, 1][:n] # result holder
    for i in range(n): 
        result.append(sum(result[-2:])) # find the sum of last 2 numbers to append the next element 
    return result

"A function to list all Armstrong numbers with a range"
def allArmstrong(inpRange): 
    def isArmstrong(inpNum):
        result = 0 # result initialized with 0
        # iterate through the string version of the number 
        for number in str(inpNum): 
            # now make the elm to int and rasie power to the length then add to result 
            result += int(number) ** len(str(inpNum))

        # now return the comparison of the original and result value 
        return result == inpNum
    # interate through the given range and use list compression and apply isArmstrong() function   
    return [i for i in range(inpRange + 1) if isArmstrong(i)] 