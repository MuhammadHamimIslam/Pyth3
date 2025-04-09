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