"method overloading"
class findSum(): 
    from multipledispatch import dispatch
    """this module has a @dispatch decorator.
    If we want to work with 2 property we can simply do -> @dispatch(type, type)
    """
    # if 2 number 
    @dispatch(int, int)
    def add(self, a, b): 
        return a + b
    # if 3 numbers 
    @dispatch(int, int, int)
    def add(self, a, b, c): 
        return a + b + c
    
# instance of the findSum class
inst = findSum()
print(inst.add(10, 20))
print(inst.add(10, 20, 30))

"dynamic binding"
# a concept of polymorphism 

class rectangle: 
    def draw(self): 
        print("A rectangle is drawn")
class square: 
    def draw(self): 
        print("A square is drawn")

def drawShape(shape): 
    shape.draw()

# instances 
rect = rectangle()
sqr = square()
# draw shape now
drawShape(rect)
drawShape(sqr)

"Abstraction"
# Abstraction is a process in which only the relevant data about an object is exposed, and hided all the other details
class food:
    def __wash(self): # wash all ingredients 
        print("Ingredients are being washed")
    def __addIngredients(self): # add all ingredients 
        print("All ingredients are added")
    def __cook(self): #finish cooking 
        print("Cooking is finished")
    def prepareFood(self): # final function that calls all sub function to finish the food preparation
        self.__wash()
        self.__addIngredients()
        self.__cook()
    # As the sun functions are private, We can't call it from outside of the class

Rice = food()
Rice.prepareFood()

"Inner class"
# inner class mean class inside a class
class Bangladesh: 
    def __init__(self, area, population):
        self.area = area
        self.population = population
        self.divisionName = self.divisions().names # get the division's name using slef.InnerClass().property 
        self.division = self.divisions().division # get all division num
    # representative of objects 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.area}', '{self.population}', {self.divisionName}, {self.division})"
    # inner class
    class divisions: 
        def __init__(self):
            self.names = sorted(["Dhaka", "Barishal", "Khulna", "Chittagong", "Rajshahi", "Mymensingh", "Rangpur", "Sylhet"])
            self.division = self.names.__len__()

bd = Bangladesh("147570km", "168M")
print(bd)

"Anonymous class"
# python doesn't have built in anonymous class but we can dynamically create it using type() function 
# syntac: class = type(name, (baseClass), attribute / method, {methods})
methods = {
    "intro": lambda self: "I'm an anonymous class!", # intro method 
    "__init__": lambda self, name: setattr(self, "name", name), # init method 
    "__repr__": lambda self: f"{self.__class__.__name__}('{self.name}')"
    } # defining method/properties for anonymous class 

anonymousClass = type("anonymousClass", (), methods)

anoyObj = anonymousClass("Anonymous Class")
print(anoyObj)

"Singleton Class"
# singleton class is a class where ony 1 object can be created from the class. If multiple is created the first will be counted 
"-> using __init__()"
class singleton1: 
    __instance = None # singleton instance holder
    @staticmethod
    def createInstance(self):
        # static method to create an instance 
        if singleton1.__instance == None:
            # if no instance is present, create one 
            singleton1()
        # return the previous or new created instance 
        return singleton1.__instance
    # constructor to initialize the singleton instance
    def __init__(self, info):
        # if an instance is already present raise an error (Exception)
        if singleton1.__instance != None:
            raise Exception("Object exists!")
        else:
            # if instance isn't present already, set it to current object (self) 
            singleton1.__instance = self
        # property of the class
        self.info = info
        
obj1 = singleton1("It's a singleton object")

print(obj1.__dict__)

"-> using __new__() function"

class singleton2: 
    __instance = None
    # __new__() function creates new instances for a class
    def __new__(cls):
        # check if instance is present
        if singleton2.__instance is None:
            # if object not present the create one
            cls.__instance = super(singleton2, cls).__new__(cls)
        else: #if object is found then raise an error 
            raise Exception("Obj exists")
        return singleton2.__instance
    
obj2 = singleton2()

"Wrapper class"

