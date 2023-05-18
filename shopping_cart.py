class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:

    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                break

    def checkout(self):

        total_price = 0
        for item in self.items:
            total_price += item.price
        self.items = []
        return round(total_price, 2)  # Round the total price to 2 decimal places
    
item1 = Item("Item 1", 10.99)
item2 = Item("Item 2", 5.99)
cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
print("Items in the cart:")
for item in cart.items:
    print(item.name)
print("Total price:", cart.checkout()) 