class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def checkout(self):
        total_price = sum(item.price for item in self.items)
        self.items = []
        return round(total_price, 2)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, ${self.price}"

item1 = Item("Apples", 10.99)
item2 = Item("Oranges", 5.99)

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)

# Create a list of dictionaries to hold the cart items
items_dict_list = []
for item in cart.items:
    items_dict_list.append({"name": item.name, "price": item.price})

# Print the items in the cart as a list of dictionaries
print("Items in the cart:")
print(items_dict_list)

# Print the total price
print("Total price:", cart.checkout())
