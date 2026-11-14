# class Order:
#     # self --> refer to the particular object in which the method is being called.
#     def show_order(self): # a method is a function defined inside the class
#         print("Customer:", self.customer)
#         print("Amount:", self.amount)
#         print("Payment Status:", self.payment_status)

# # Create first order (object)
# order_1 = Order()
# order_1.customer ="Ali"
# order_1.amount = 5000
# order_1.payment_status = "Paid"

# # Create second order
# order_2 = Order()
# order_2.customer = "Ahmed"
# order_2.amount = 8000
# order_2.payment_status = "Pending"

# # Call methods
# order_1.show_order()
# print("-------------")
# order_2.show_order()

# why use: self.customer --> because we want the customer attributes belonging to the particular object.


# NOW We update our code:
# constructor (__init__) --> A constructor is a special method that python automatically calls when we create an object. its purpose is to intialize the object's attributes.

class Order:
    def __init__(self, customer, amount, payment_status):
        self.customer = customer
        self.amount = amount 
        self.payment_status = payment_status
    def show_order(self):
        print("Customer: ", self.customer) # customer on the right: the parameter receiving the value. 
        # self.customer on the left: the attributes stored inside the current object. 
        print("Amount: ", self.amount)
        print("Payment Status: ", self.payment_status)
# __init__: Special method called automatically during object initialization.
# self: Refers to the object being initialized.
# customer, amount, payment_status: Parameters receiving the data supplied when creating the object.

# Creating objects with their own information

order_1 = Order("Bilal", 12000, "Paid")
order_2 = Order("Usman", 7500, "Pending")

print("Order 1:", order_1.customer, order_1.amount)
print("Order 2:", order_2.amount, order_2.amount)

order_1.payment_status = "Refunded"
print("Orders Payment statuses: ", order_1.payment_status, order_2.payment_status)

# Display orders

order_1.show_order()
print("-------------")
order_2.show_order()

# How do python know which value belong to which parameter?
# Python matches positional arguments to parameters according to their order. The mapping is:
# Argument	Parameter
# "Ali"	    customer
# 5000	    amount
# "Paid"	payment_status
