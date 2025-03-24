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
