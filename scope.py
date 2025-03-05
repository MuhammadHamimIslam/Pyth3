x = 10 # x is a global variable 

def fun1 (): 
  print(f"x inside the function: {x}") # prints 10 as no local variable is present
fun1() 
print(f"x globally: {x}\n") # prints 10

def fun2 (): 
  x = 20 # this x is a local variable 
  print(f"x inside the function: {x}") 
fun2() # prints 20 as there's a local variable 
print(f"x globally: {x}\n") # prints 10

def outer1(): 
  x = 20 # x is a local variable available inside the function only
  print(f"x inside the outer function: {x}")  
  def inner():
    print(f"x inside the inner function: {x}")  # prints 20 as there's no variable inside the function 
  inner()
outer1()  
print(f"x globally: {x}\n") # prints 1p

def outer2():
  global x # this changes the scope of x to global 
  x = 20 
  print(f"x inside the outer function: {x}") # prints 20
  def inner():
    print(f"x inside the inner function: {x}")  # prints 20
outer2()
print(f"x globally: {x}\n") # prints 10

def outer3():
  global x # this changes the scope of x to global 
  x = 20 
  print(f"x inside the outer function: {x}")  # prints 20
  def inner():
    x = 30
    print(f"x inside the inner function: {x}")    # prints 30
  inner()
outer3()    
print(f"x globally: {x}\n") # prints 20

def outer4():
  x = 20 
  print(f"x inside the outer function: {x}")  # prints 20
  def inner():
    global x # this changes the scope of x to global 
    x = 30
    print(f"x inside the inner function: {x}")    # prints 30
  inner()
outer4()    
print(f"x globally: {x}\n") # prints 30

def outer5():
  x = 20 
  print(f"x inside the outer function: {x}")  # prints 20
  def inner():
    nonlocal x # this changes the scope of x to local but not global 
    x = 30
    print(f"x inside the inner function: {x}")    # prints 30
  inner()
outer5()    
print(f"x globally: {x}\n")

