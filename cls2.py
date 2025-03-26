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

