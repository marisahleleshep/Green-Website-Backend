# Define a class called Customer
class Discount:
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
customer1 = Discount("Mwangi", "mwangi@gmail.com", "Kasarani", "5234-456-987")
customer1.add_purchase(120)
print(customer1.total_purchase)  
print(customer1.preference(8))  
print(customer1.discount())  
customer1.remove_purchase(50)
print(customer1.total_purchase)  


