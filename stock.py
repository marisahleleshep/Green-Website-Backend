# Define a class called Stock
class Stock:
    # Define the constructor method to initialize the Mama_Mboga object
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.action = action

    # Define a method to update the product name
    def new_stock(self, new_product):
        self.product_name = new_product
        return f"{self.product_name}"

    # Define a method to update the quantity of products
    def quantity_products(self, new_quantity):
        self.quantity = new_quantity
        return f"{self.quantity}"

    # Define a method to update the price of the product
    def update_price(self, new_price):
        self.price = new_price
        return f"{self.price}"

    # Define a method to update the action associated with the product
    def product_ripen(self, action):
        self.action = action
        return f"{self.action}"

    # Define a method to display the Mama_Mboga object as a string
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"


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












 









