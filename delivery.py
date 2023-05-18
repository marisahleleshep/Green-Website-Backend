class Order:
    
    def __init__(self,order_time,expected_delivery_time,expected_delivery_location,user,status):
   
       self.order_time = order_time
       self.expected_delivery_time= expected_delivery_time
       self.expected_delivery_location=expected_delivery_location
       self.user=user
       self.status=status
     
    def order_time(self):
        return self.order_time
    # returns the value of the delivery_time
    def expexted_delivery_time(self):
        return self.delivery_time
    #  returns the value of the delivery location
    def expected_delivery_location(self):
        return self.delivery_location
    # status method allows updating the status attribute with a new value.
    def set_status(self, status):
        self.status = status
        
    
order1= Order("order_time =2023-5-13-8:00", "expected_delivery_time=2023-5-13:2:00", "expected_delivery_location=Kangemi junction", "user=Naima mohamed", "status=deliver")  
  
class OrderTracker:
    def __init__(self):
        self.orders = []
    #  method takes an order  as a parameter and removes it from the orders list.
    def remove_order(self, order):
        self.orders.remove(order)
        
        #add order method takes an order object as a parameter and appends it to the orders list.
    def add_order(self, order):
        self.orders.append(order)
        
        # The get_orders method returns the list of orders stored in the orders attribute.
    def get_orders(self):
        return self.orders
    
    # The track_order method takes an order object as a parameter and
    # prints various details related to that order 
    def track_order(self, order):
        
        print("User:", order.user())
        print("Time Ordered:", order.time_ordered())
        print("Delivery Time:", order.expected_delivery_time())
        print("Delivery Location:", order.expected_delivery_location())
        print("Order Status:", order.status())










