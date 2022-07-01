#!/usr/bin/python3
class Item:
    rate = 0.9
    def __init__ (self, name: str, price: float, quantity):
        #run validations
        
        assert price >= 0, f"price {price} is less than 0"
        assert quantity >= 0, f"quantity {quantity} is less than 0"
        
        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_rate (self):
        self.price = self.price * self.rate
        
item1 = Item("cars", 100, 3)

item2 = Item("bikes", 1000, 4)

item1.apply_rate()
print(item1.price)

item2.rate = 0.7
item2.apply_rate()
print(item2.price)