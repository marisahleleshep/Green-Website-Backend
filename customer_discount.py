# Define a class called Customer
class Discount:
    def __init__(self, name, email, location, phoneNumber):
        self.name = name
        self.email = email
        self.location = location
        self.phoneNumber = phoneNumber
        self.total_purchase = 0

    def discount(self):
        if self.total_purchase >= 100:
            return 0.1 * self.total_purchase
        else:
            return 0

    def add_purchase(self, amount):
        if amount > 0:
            self.total_purchase += amount
        else:
            print("Insufficient purchase amount")

    def remove_purchase(self, amount):
        if amount <= self.total_purchase:
            self.total_purchase -= amount
        else:
            print("The amount is greater than the total purchase.")


customer1 = Discount("Mwangi", "mwangi@gmail.com", "Kasarani", "5234-456-987")
customer1.add_purchase(120)
print(customer1.total_purchase)
print("Discount: ", customer1.discount())
customer1.remove_purchase(50)
print(customer1.total_purchase)
