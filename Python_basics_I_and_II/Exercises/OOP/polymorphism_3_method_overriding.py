# Method overriding: A child class defined a method with the same name is the parent. 
# The child's version replaces the parent.
# It allows child class to provide a specific implementation for a method that is already defined in its parent class.

# # Exercise no: 1
# class Shipping:
#     def calculate_cost(self):
#         return 300
# class ExpressShipping(Shipping):
#     def calculate_cost(self):
#         return 700

# order1 = Shipping()
# order2 = ExpressShipping()

# print(order1.calculate_cost())
# print(order2.calculate_cost())

# Exercise 4 -- Independent practical task:
class Payment:
    def process_payment(self):
        print("General payment processing")
class CardPayment(Payment):
    def process_payment(self):
        print("Process card payment")
class CashOnDelivery(Payment):
    def process_payment(self):
        print("Processing cash on delivery")

order1 = Payment() # here () -- tells python to call the class to crate an instance, we write Payment, we are not creating an object.
order2 = CardPayment()
order3 = CashOnDelivery()

order1.process_payment() # here () --> tells python to execute the method.
order2.process_payment()
order3.process_payment()