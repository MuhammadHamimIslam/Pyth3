class item:
    discount = 0.2 # discount is set to 20%
    def __init__(self, name: str, price: float, quantity = 0):
        # validate input
        """We can validate the input parameter by using assert statement.
        assert statement works like -> 
        assert condition, 'Error Message'
        """
        assert price > 0, f"Price can't be 0 or negative"
        assert quantity >= 0, "Quantity can't be 0 or negative"
        self.name = name
        self.price = price 
        self.quantity = quantity
    def totalPrice(self):
        self.applyDiscount() # apply the discount 
        return self.price * self.quantity
    def applyDiscount(self):
        """
        return self.price * discount
        this will raise an error because we can only access a variable using instance or class level
        """
        rateOfPay = (1 - self.discount)
        self.price *= rateOfPay

item1 = item("Rice", 50, 10)
item2 = item("Meat", 800, 5)
item3 = item("Vegetable", 45, 1)

print(f"Total price of meat after 20% discount: {item1.totalPrice()}")

"""What if we want to apply different discount for each item?
Then need to change the discount from instance level then apply different discount
"""
# If we want to apply 30% discount for Meats then we'll change it from instance level 
item2.discount = 0.3
print(f"Total price of meat after 30% discount: {item2.totalPrice()}")

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

"listing all instances of a class"

class hero: 
    heros = [] # result holder
    def __init__(self, name, rank):
        # adding properties 
        self.name = name 
        self.rank = rank
        # adding all instances to list
        hero.heros.append(self)
    def __repr__(self): # representative of objects 
        return f"hero('{self.name}', {self.rank})"

hero1 = hero("a", 3)
hero2 = hero("b", 4)
hero3 = hero("c", 2)
hero5 = hero("d", 1)

print(hero.heros) # returns all heros

"class inheritance"

"-> Single inheritance"
# parent class
class parent: 
    def parentMethod(self): # a parent method 
        print("This is a parent method")

# child class
class child(parent): 
    def childMethod(self): 
        print("This is a child method")

# a child object 
child1 = child()
# by using child object, we can access both parent and child method, variables, function
child1.childMethod()
child1.parentMethod()

"-> Multiple inheritance"

class parent1: # parent 1 class
    def parent1Method(self): 
        print("I'm parent1")
class parent2: # parent 2 class
    def parent2Method(self):
        print("I'm parent2")
#child class inherits both parent1 & parent2
class myChild(parent1, parent2): 
    def childMethod(self): 
        print("I'm a child")

myChildObj = myChild() # object from the child
myChildObj.parent1Method() # gets parent1
myChildObj.parent2Method() # gets parent2
myChildObj.childMethod() # gets child

"-> multi level inheritance"

class world: # a parent class 
    def worldMethod(self): 
        print("I'm the entire world!")
class Bangladesh(world): # Bangladesh class inherits from world 
    def bangladeshMethod(self): 
        print("I'm Bangladesh 🇧🇩")
class Dhaka(Bangladesh): # Dhaka that inherits both Bangladesh and world 
    def dhakaMethod(self): 
        print("Dhaka is the capital of Bangladesh")

DhakaCity = Dhaka() # object from Dhaka 
DhakaCity.worldMethod()
DhakaCity.bangladeshMethod()
DhakaCity.dhakaMethod()

"super() function"

class person: # person class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def email(self): 
        return f"{self.name}.{self.age}@gmail.com"
class student(person): # student is also a person. so it inherits person class
    def __init__(self, name, age, idNo):
        # using super() we can inherit any property from parent class
        super().__init__(name, age) 
        self.idNo = idNo

student1 = student("pqr", 15, "123ji")
print(student1.__dict__)
print(student1.email())

"polymorphism"
