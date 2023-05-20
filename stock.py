class Stock:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    def update_price(self, new_price):
        self.price = new_price
    def display_stock(self):
        print(f"Stock Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        # Creating a new stock object
stock_item = Stock("Apples", 100, 2.5)
# the initial stock details
stock_item.display_stock()
# Updating the stock quantity
stock_item.update_quantity(80)
# Updating the stock price
stock_item.update_price(2.0)
# display of the the updated stock details
stock_item.display_stock()
