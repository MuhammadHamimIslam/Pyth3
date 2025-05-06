"A Decorator in Python is a function that receives another function as argument"

# decorator is a way to add extra information to a function without modifying the original function 

# decorator function 
def myDecorator(func): 
    def wrapper ():
        print("It's called at first!")
        # call the decorator 
        func()
        print("It's called at last!")
    return wrapper
    
@myDecorator
# the function that we want to decorate 
def sayHello():
    print("Hello everyone, What's up?")

# call the decorator 
sayHello()