# # Abstraction: Defining what an object must do, not how it does it

# # Abstract Class (ABC): A class that cannot be instantiated while abstract methods remain unimplemented.

# # Abstract method: A method marked with @abstractmethod. forces sub-class to implement required behavior

# from abc import ABC, abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def process_payment(self):
#         pass
    

# class JazzCash(PaymentGateway):
#     def process_payment(self):
#         print("Processing JazzCash Payment")
#     def verify_mobile_account(self):
#         print("Verifying mobile wallet")
# class Stripe(PaymentGateway):
#     def process_payment(self):
#         print("Processing Stripe Payment")
#     def verify_card(self):
#         print("Verifying Stripe Card")
# class Paypal(PaymentGateway):
#     def process_payment(self):
#         print("Processing Paypal payment")
#     def verify_paypal_account(self):
#         print("Verifying Paypal account")
# class EasyPaisa(PaymentGateway):
#     def process_payment(self):
#         print("Processing Easypaisa payment")

# def checkout(gateway):
#     print("Starting checkout....")
#     gateway.process_payment()

# order1 = JazzCash()
# order2 = Stripe()
# order3 = Paypal()
# order4 = EasyPaisa()

# checkout(order1)
# checkout(order2)
# checkout(order3)
# checkout(order4)


# # order1.process_payment()
# # order1.verify_mobile_account()
# # print("----------------------")
# # order2.process_payment()
# # order2.verify_card()
# # print("----------------------")
# # order3.process_payment()
# # order3.verify_paypal_account()


# # Benefit	        Technical meaning
# # Consistency	    All providers follow the same required interface.
# # Reusability	    The same orchestration logic works with multiple providers.
# # Maintainability   Changes to one provider need not affect others.
# # Extensibility	    New providers can be added without rewriting checkout logic.
# # Loose coupling    Checkout depends on the common interface, not specific provider implementations.


