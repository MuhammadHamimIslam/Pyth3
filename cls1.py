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

"Public, Private, Protected variable"

class person: 
    def __init__(self, name, age, idNo):
        self.name = name # public variable can be accessed any time 
        self._age = age # with one _, it's protected variable 
        self.__idNo = idNo # with double __, it's private variable
        
person1 = person("XYZ", 23, "1oxyxP0001")
print(person1.name)
print(person1._age)
# print(person1.__idNo) will raise an error because of being a private variable 
# to access it we need (obj._class__var)
print(person1._person__idNo)

"property object"
class student: 
    def __init__(self, name, age):
        self.__name = name # private var
        self.__age = age # private var
    # function for getting name
    def getName(self):
        return self.__name
    # function for getting age
    def getAge(self):
        return self.__age
    # function for setting name 
    def setName(self, name):
        self.__name = name
    # function for setting age
    def setAge(self, age):
        self.__age = age
    # now set property 
    name = property(getName, setAge, "name")
    age = property(getAge, setAge, "age")

student1 = student("xyz", 15)
print(f"student's name is: {student1.name}")

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
    i = 0
    @classmethod
    def say(): 
        print("Tree is very important for us.")

# defining method  
@classmethod
def treeCount(self):
    self.i += 1 # increase count by 1
    print(f"tree count {self.i}")

# adding method 
setattr(tree, "count", treeCount)

mangoTree = tree()
print(mangoTree.count())

"dynamically delete attribute"
del tree.say # deletes the attribute 

"static methods of class"



"Build in class attributes"

print(phone.__dict__) # convert to a dictionary from the class's namespace 
print(phone.__doc__) # returns tje docstrings inside the class
print(phone.__name__) # returns the class's name
print(phone.__module__) # returns the module where the class is defined 
print(phone.__bases__) # returns the base class
