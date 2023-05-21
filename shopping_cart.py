import delivery
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.item=[]

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
        return round(total_price, 2)

item1 = Item("Berries", 10.99)
item2 = Item("Pawpaw", 5.99)
cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
print("Items in the cart:")
for item in cart.items:
    print(item.name)
print("Total price:", cart.checkout())

# added the dictionary to show orders the customer has made
orders = {
    "customer_name": "John",
    "items": {
        item1.name: item1.price,
        item2.name: item2.price
    },
    "total_price": cart.checkout()
}
print(orders)
