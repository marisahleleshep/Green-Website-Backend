import datetime
from customer_order import customers_name
from customer_order import ccustomer_address
from customer_order import order_items

from shopping_cart import order_items


class Order:


  def __init__(self, id, order_date, order_total):
    self.id = id
    self.order_date = order_date
    self.order_total = order_total

  def get_delivery_status(self):
  

    delivery_status = {
      "id": 1273944,
      "customer_order_id": self.id,
      "delivery_date": self.order_date,
      "delivery_time": "12:45 noon",
      "delivery_status": "Delivered",
      "delivery_address": self.customer_address,
    }
    return delivery_status


# Create a customer order
customer_order = Order(
  id=1273944,
  customer_name="Khadija Rihami",
  customer_address="123 Makutex Street, Starehe, Kongoea",
  order_date=datetime.date(2023, 5, 21),
  

# Get the delivery status
delivery_status = customer_order.get_delivery_status()

print(f"Delivery Status\nOrder ID: {delivery_status['customer_order_id']}\nDelivery Date: {delivery_status['delivery_date']}\nDelivery Time: {delivery_status['delivery_time']}\nDelivery Status: {delivery_status['delivery_status']}\nDelivery Address: {delivery_status['delivery_address']}")
