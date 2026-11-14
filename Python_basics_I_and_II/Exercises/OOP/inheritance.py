# Definition: An Object-Oriented Programming (OOP) mechanism where a Child Class (subclass) automatically receives (inherits) the attributes and methods of a Parent Class (super class).

# The "Is-A" Relationship: A child object is a type of parent object (e.g., a ShopifyStore or DigitalOrder is a specific type of Order).

# Primary Benefit (Code Reusability): Eliminates duplicate code by writing shared logic once in the parent class and sharing it across multiple child classes.

#  Single Inheritance
# Definition: A single child class inherits directly from one parent class.
# Key Characteristic: Forms a simple two-tier relationship (Parent --> Child).
# Example Structure:
# class Order: # parant class
#     def display(self):
#         print("Displaying order...")
# class DigitalOrder(Order):
#     def download(self):
#         print("Downloading file...")


# Shopify Order Management system:
class Order:
    def __init__(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount
    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer}")
        print(f"Amount: {self.amount}")
class PhysicalOrder(Order):
    def prepare_shipment(self):
        print(f"Order preparing for shipment")
class DigitalOrder(Order):
    def provide_download(self):
        print("providing download access ...")
# Python recognizes each object's class as a sub-class of Order. therefore, each object qualifies as an instance of Order.
class SubscriptionOrder(Order): 
    def activate_subscription(self):
        print("Activating subscription...")

order1 = PhysicalOrder(1001, "Behram", 5500)
order2 = DigitalOrder(1002, "Rashid", 4500)
order3 = SubscriptionOrder(1003, 'Hameed', 3500)

order1.display_order()
order1.prepare_shipment()
print("------------------")
order2.display_order()
order2.provide_download()
print("------------------")
order3.display_order()
order3.activate_subscription()

print(isinstance(order1, Order))
print(isinstance(order2, Order))
print(isinstance(order3, Order))

# - Inheritance gives a child class access to inherited functionality.
# - The inheritance relationship also establishes an is-a relationship.
# - isinstance() checks whether an object belongs to a class or one of its subclasses.