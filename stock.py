# Define a class called Stock
class Stock:
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.action = action
    def new_stock(self, new_product):
        self.product_name = new_product
    def quantity_products(self, new_quantity):
        self.quantity = new_quantity
    def update_price(self, new_price):
        self.price = new_price
    def product_ripen(self, action):
        self.action = action
    def __str__(self):
        return f"{self.product_name}, {self.quantity}, {self.price}, {self.action}"
# Create an instance of the class Stock
vendor = Stock("Potatoes", 50, 2.99, "Sell")
print(vendor)
vendor.new_stock("Kales")
print(vendor)
vendor.quantity_products(100)
print(vendor)
vendor.update_price(190)
print(vendor)
vendor.product_ripen("Restock")
print(vendor)
