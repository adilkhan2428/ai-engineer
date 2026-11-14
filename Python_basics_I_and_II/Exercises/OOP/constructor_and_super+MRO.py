# Constructor Overriding: when we create a child class, python looks for a constructor (__init__) in the child class first, it it missing then it reaches back to the parant class

# super(): this is used inside a child class to explicitly call the parant's constructor or methods. it have some scenerio: below:

# Situation	                                 Behavior
# Child has its own method	                 Child method executes.
# Child has its own method and calls super()	Child and parent methods execute.
# Child has its own method without super()	 Only child method executes.
# Child has no method	                     Inherited parent method executes.

# MRO: In multiple inheritance when the child have multiple parant classes, python follows a "left-to-right" rule. it execute the first parant class. even if both parant class have same methods


# Exercise 1: Build an Order Inheritance System:
# Create two classes:
# class Order:  # parant class
#     def __init__(self, order_id, customer_name, amount):
#         self.order_id = order_id
#         self.customer_name = customer_name
#         self.amount = amount

#     def display_order(self):
#         print("Order ID:", self.order_id)
#         print("Customer Name:", self.customer_name)
#         print("Amount:", self.amount)


# class ShopifyOrder(Order):
#     def __init__(self, order_id, customer_name, amount, payment_status):
#         super().__init__(order_id, customer_name, amount)
#         self.payment_status = payment_status

#     def display_order(self):
#         super().display_order()
#         print(f"Payment Status: {self.payment_status}")


# order = ShopifyOrder(1001, "Adil", 5500, "Paid")

# order.display_order()

# Exercise 2 -- Multiple Inheritance in an E-commerce System
# # Scenerio: Our e-commerce platform has two independent capabilities:
# class InventoryManagement:
#     def check_stock(self):
#         print("Checking product inventory")
# class PaymentProcessing:
#     def process_payment(self):
#         print("Processing customer payment")
# class ShopifyStore(InventoryManagement, PaymentProcessing):
#     pass

# order = ShopifyStore()
# order.check_stock() 
# order.process_payment()
# # This is inheritance-based method lookup.


# Exercise 3 -- Understanding MRO in Multiple Inheritance
# class InventoryManagement:
#     def get_status(self):
#         print("Inventory status")

# class PaymentProcessing:
#     def get_status(self):
#         print("Payment status")

# class ShopifyStore(InventoryManagement, PaymentProcessing):
#     pass

# store = ShopifyStore()
# store.get_status()

# Exercise 4 - Integrated practical challange
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount
    def display_order(self):
        print("Order ID:", self.order_id)
        print("Amount:", self.amount)
class PaymentProcessing:
    def process_payment(self):
        print("payment processed successfully")
class ShopifyOrder(Order, PaymentProcessing):
    def __init__(self, order_id, amount, status):
        super().__init__(order_id, amount)
        self.status = status
    def display_order(self):
        super().display_order()
        print("Payment Status:", self.status)

order = ShopifyOrder(1001, 4500, "Paid")

order.display_order()
order.process_payment()