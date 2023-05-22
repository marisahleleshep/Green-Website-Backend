import datetime

class Customer_Order:


  def __init__(self, customer_name, customer_address, order_date, order_items, order_total):
    self.customer_name = customer_name
    self.customer_address = customer_address
    self.order_date = order_date
    self.order_items = order_items
    self.order_total = order_total

  def get_delivery_status(self):
  

    delivery_status = {
      "customer_order_id": self.id,
      "delivery_date": self.order_date,
      "delivery_time": "12:45 noon",
      "delivery_status": "Delivered",
      "delivery_address": self.customer_address,
    }
    del delivery_status["customer_order_id"]
    return delivery_status


# Create a customer order
customer_order = Customer_Order(
  customer_name="Khadija Rihami",
  customer_address="123 Makutex Street, Starehe, Kongoea",
  order_date=datetime.date(2023, 5, 21),
  order_items=[
    {
      "product_id": 6,
      "product_name": "cauliflower",
      "product_quantity": 4,
      "product_price": 200.00,
    },
    {
      "product_id": 2,
      "product_name": "Cabbages",
      "product_quantity": 4,
      "product_price": 300.00,
    },
  ],
  order_total=500.00,
)

# Get the delivery status
delivery_status = customer_order.get_delivery_status()

print(f"Delivery Status\nDelivery Date: {delivery_status['delivery_date']}\nDelivery Time: {delivery_status['delivery_time']}\nDelivery Status: {delivery_status['delivery_status']}\nDelivery Address: {delivery_status['delivery_address']}")
