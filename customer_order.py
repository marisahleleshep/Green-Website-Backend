# Define a class called Order
from delivery import order_items
from delivery import customer_name
class Order:
    def __init__(self,customer_email, order_date):
        self.customer_email = customer_email
        self.order_date = order_date
     

    def get_order_details(self):
        print("Order details for customer:", self.customer_name)
        print("Email:", self.customer_email)
        print("Order date:", self.order_date)
        print("Order items:")
        for item in self.order_items:
            print(item)

# Create an order
order = Order("Mwangi", "mwangi@gmail.com", "2023-05-20", ["Apples", "Oranges"])

# Get the order details
order.get_order_details()
