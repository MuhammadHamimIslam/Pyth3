"A class is an object constructor, a blueprint for creating object"

"defining a class"

class myClass: 
    var = 100
 
"accessing an obj inside a class"
myObj = myClass()

print(f"variable in class is: {myObj.var}")

"creating an object using class"
class product: 
    def calcTotalPrice(self, qunt, price): 
        return qunt * price
        
# adding data to the object 
product1 = product()
product1.name = "watch"
product1.quantity = 12
product1.price = 100
product1.totalPrice = product1.calcTotalPrice(product1.quantity, product1.price)

print(product1.totalPrice)

"Adding data using constructor (__int__)"

class phone:
    "A simple class to create phone objects"
    # adding data to the object 
    def __init__(self, name: str, model: str, price: float, quantity = 0):
        # validate input
        """We can validate the input parameter by using assert statement.
        assert statement works like -> 
        assert condition, 'Error Message'
        """
        assert price > 0, f"Price can't be 0 or negative"
        assert quantity >= 0, "Quantity can't be 0 or negative"
        self.name = name
        self.model = model
        self.price = price 
        self.quantity = quantity
    
    def totalPrice(self): 
        return self.price * self.quantity

# now just have to pass the data as parameter
Samsung = phone("Samsung", "S24 Ultra", 350, 5)
print(f"Samsung's name: {Samsung.name}")
print(f"Total Price is: {Samsung.totalPrice()}")

iPhone = phone("iPhone", "16 Pro Max", 550, 2)
print(f"iPhone's name: {iPhone.name}")
print(f"Total Price is: {iPhone.totalPrice()}")


"Some functions for classes"

"-> hasattr(obj, name) to check if an attribute is present"
print(hasattr(iPhone, "model")) # returns true if "mode" attribute is present 

"-> getattr(obj, name) to get the attribute"
print(getattr(iPhone, "name")) # returns tje "name" attribute 

"-> setattr(obj, name, value) to set a new attribute"
setattr(iPhone, "model", "17 pro max") # sets "model" to 17 pro max 
print(f"{iPhone.model = }")

"-> delattr(obj, property) to delete an attribute"
delattr(Samsung, "price") # deletes the price
print(Samsung.__dict__) # there's no longer price's present 

"dynamically add class methods"

"using @classmethod"
class tree: # an empty class
    treeNum = 0

# adding method dynamically  
@classmethod
def treeCount(clss): 
    # increase the tree count whenever it's being called 
    clss.treeNum += 1


"Build in class attributes"

print(phone.__dict__) # convert to a dictionary from the class's namespace 
print(phone.__doc__) # returns tje docstrings inside the class
print(phone.__name__) # returns the class's name
print(phone.__module__) # returns the module where the class is defined 
print(phone.__bases__) # returns the base class

"magic method of class"
"Magic methods are automatically called whenever the class is used"

class shape:
    # data of object 
    def __init__(self, name: str, length: int, width: int, height = 0):
        # adding data to object 
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        
        # data validation 
        assert length >= 0, f"length can't be less than or equal to zero!"
        assert width >= 0, f"width can't be less than or equal to zero!"
    # custom string representation 
    def __str__(self): 
        return f"It's a {self.name}. It's length is {self.length}, width is {self.width} and height is {self.height}"
    # addition 
    def __add__(self, other):
        return self.length + other.length
    # less than 
    def __lt__(self, other):
        return self.width < other.width
    # greater than 
    def __gt__(self, other):
        return self.length > other.length 
# all objects     
shape1 = shape("square", 100, 100)
shape2 = shape("rectangle", 120, 80)
shape3 = shape("cube", 90, 90, 90)

"-> __str__ method"
# if we print shape1, we'll see the memory addresses of the object not the information. By using __str__ method we can define what we'll see
print(shape1)

"-> __add__ method"
# if we try to add any value of a object, we'll get an error. By using __add__ method we can define it
print(f"The sum of lengths is: {shape1 + shape2}")

"-> __lt__ method"
# if we try to use ">" to compare 2 objects, we'll get an error. By using __lt__ method we can define it
print(shape1 < shape2)

"-> using __gt__ method"
# if we try to use "<" to compare 2 objects, we'll get an error. By using __gt__ method we can define it
print(shape1 > shape2)

