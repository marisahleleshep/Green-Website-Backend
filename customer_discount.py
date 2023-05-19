

# create class discount for a customer
class Discount:
    def __init__(self, discount_type, discount_amount):
        self.discount_type = discount_type
        self.discount_amount = discount_amount
    
    def apply_discount(self, total):
        if self.discount_type == 'percentage':
            discounted_total = total * (1 - self.discount_amount / 100)
        else:
            discounted_total = total - self.discount_amount
        return discounted_total
    
    def get_discounted_price(self, price):
        if self.discount_type == 'percentage':
            discounted_price = price * (1 - self.discount_amount / 100)
        else:
            discounted_price = price - self.discount_amount
        return discounted_price
    # create a new instance of the Discount class
discount = Discount('percentage', 20)

# get the discounted price of a product
price = 100
discounted_price = discount.get_discounted_price(price)
print(f"The discounted price of the product is: {discounted_price}"


