try:
  num1 = int(input("Enter number1: "))
  num2 = int(input("Enter number2: "))
  
  print("The result is", num1 / num2)
  
except ValueError: # if user gives input a innumeric value(that causes ValueError), this except block will be executed else ignored
  print("Enter a numeric value!")
  
except ZeroDivisionError: # if the 2nd number is 0 (ZeroDivisionError), this except block will be executed 
  print("Can't divide by 0!")