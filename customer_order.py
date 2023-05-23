
# Define a class called Order
class Order:
    def __init__(self, customer_name, customer_email, order_date, order_items):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.order_date = order_date
        self.order_items = order_items

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
