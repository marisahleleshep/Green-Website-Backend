# Define a class called Customer
class Customer:
    # Define the constructor method to initialize the Customer object
    def __init__(self, name, email, location, phoneNumber):
        self.name = name
        self.email = email
        self.location = location
        self.phoneNumber = phoneNumber
        self.total_purchase = 0

    # Define a method to calculate the discount based on total purchases
    def discount(self):
        if self.total_purchase >= 100:
            return 0.1
        else:
            return 0

    # Define a method to add a purchase amount to the total purchase
    def add_purchase(self, amount):
        self.total_purchase += amount

    # Define a method to remove a purchase amount from the total purchase
    def remove_purchase(self, amount):
        if self.total_purchase >= amount:
            self.total_purchase -= amount
        else:
            print("The amount is greater than the total purchase.")

    def preference(self, num):
        return num ** 2

# Create an instance of the Customer class
customer1 = Customer("Mwangi", "mwangi@gmail.com", "Kasarani", "5234-456-987")
customer1.add_purchase(120)
print(customer1.total_purchase)  
print(customer1.preference(8))  
print(customer1.discount())  
customer1.remove_purchase(50)
print(customer1.total_purchase)  


# Define a class called Mama_Mboga
class Mama_Mboga:
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
vendor = Mama_Mboga("Potatoes", 50, 2.99, "Sell")
print(vendor)  
vendor.new_stock("Kales")
print(vendor)  
vendor.quantity_products(100)
print(vendor)  
vendor.pricing(1.99)
print(vendor)  
vendor.update_action("Restock")
print(vendor)  











 









