
class Order:

    # Inner class
    class Shipping:
        def __init__(self, tracking_number, carrier):
            self.tracking_number = tracking_number
            self.carrier = carrier

    # Outer class constructor
    def __init__(self, customer, tracking_number, carrier):
        self.customer = customer

        # Create a Shipping object inside this Order object
        self.shipping = Order.Shipping(tracking_number, carrier)


# Create two Order objects
order1 = Order("Adil", "ABC111", "DHL")
order2 = Order("Atif", "ABC222", "FedEx")


# Access order information
print("Order 1")
print(order1.customer)
print(order1.shipping.tracking_number)
print(order1.shipping.carrier)

print("\nOrder 2")
print(order2.customer)
print(order2.shipping.tracking_number)
print(order2.shipping.carrier)
