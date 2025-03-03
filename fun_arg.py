def sayHello ():
  print("Hello!") # simple function to say hello 
sayHello()
  
def findMax (num1, num2, num3): # function with argument and return statement 
  maxNum = num1
  for i in [num1, num2, num3] : 
    if i > maxNum :
      maxNum = i
  return maxNum
maxNum = findMax(1, 9, 3)
print(maxNum)

def avg (num1 = 10, num2 = 0, num3 = 15): # function with default argument 
  return sum([num1, num2, num3]) // 3
average = avg(num3 = 3, num2 = 2)  
print(average)

def findMin (*numbers): 
  minNum = numbers[0]
  for i in numbers:
    if i < minNum: minNum = i
  return minNum
minNum = findMin(7, 8, 4, 5, 9, 11)
print(minNum)

def msg (**info):
  return f"Hey {info['name']}! You have {info['status']} in the exam."
message = msg(name = "xyz", status = "passed")  
print(message)