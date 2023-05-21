import datetime

class Customer_Order:


  def __init__(self, id, customer_name, customer_address, order_date, order_items, order_total):
    self.id = id
    self.customer_name = customer_name
    self.customer_address = customer_address
    self.order_date = order_date
    self.order_items = order_items
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
customer_order = Customer_Order(
  id=1273944,
  customer_name="Khadija Rihami",
  customer_address="123 Makutex Street, Starehe, Kongoea",
  order_date=datetime.date(2023, 5, 21),
  order_items=[
    {
      "product_id": 6,
      "product_name": "Blouse",
      "product_quantity": 4,
      "product_price": 2000.00,
    },
    {
      "product_id": 2,
      "product_name": "Body Shaper",
      "product_quantity": 1,
      "product_price": 1000.00,
    },
  ],
  order_total=3000.00,
)

# Get the delivery status
delivery_status = customer_order.get_delivery_status()

print(f"Delivery Status\nOrder ID: {delivery_status['customer_order_id']}\nDelivery Date: {delivery_status['delivery_date']}\nDelivery Time: {delivery_status['delivery_time']}\nDelivery Status: {delivery_status['delivery_status']}\nDelivery Address: {delivery_status['delivery_address']}")
