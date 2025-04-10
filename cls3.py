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
            self.division = 8

bd = Bangladesh("147570km", "168M")
print(bd)