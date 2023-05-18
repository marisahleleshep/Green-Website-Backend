# Define a class called Mama_Mboga
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

    # Define a method to update the quantity of products
    def quantity_products(self, new_quantity):
        self.quantity = new_quantity

    # Define a method to update the price of the product
    def pricing(self, new_price):
        self.price = new_price

    # Define a method to update the action associated with the product
    def update_action(self, needed_action):
        self.action = needed_action

    # Define a method to display the Mama_Mboga object as a string
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"


# Create an instance of the Mama_Mboga class
vendor = Stock("Potatoes", 50, 2.99, "Sell")
print(vendor)  
vendor.new_stock("Kales")
print(vendor)  
vendor.quantity_products(100)
print(vendor)  
vendor.pricing(1.99)
print(vendor)  
vendor.update_action("Restock")
print(vendor)  











 









