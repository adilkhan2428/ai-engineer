# this is multi-platform payment gatway systme, where we will have the one method which behave differently according to different class
# parant/base class
class PaymentProcessor:
    def __init__(self, transection_id, amount):
        self.transection_id = transection_id
        self.amount = amount
    def process_payment(self):
        raise NotImplementedError('Subclass must implement process_payment()')
# child class no. 1
class StripePayment(PaymentProcessor):
    def __init__(self, transection_id, amount, currency='USD'):
        super().__init__(transection_id, amount)
        self.currency = currency
    def process_payment(self):
        print(f"[Stripe] Processing USD transection {self.transection_id} for PKR {self.amount} via Credit Card.")
class PaypalPayment(PaymentProcessor):
    def __init__(self, transection_id, amount, email_accont):
        super().__init__(transection_id, amount)
        self.email_account = email_accont
    def process_payment(self):
        print(f"[Paypal] Charging account {self.email_account} for amount ${self.amount} securely.")
class EasypaisePayment(PaymentProcessor):
    def __init__(self, transection_id, amount, mobile_number):
        super().__init__(transection_id, amount)
        self.mobile_number = mobile_number
    def process_payment(self):
        print(f"[EasyPaise] Transeferring PKR {self.amount} to mobile {self.mobile_number} using PIN verification.")
# polymorphic execution function

def checkout_all(payments):
    for checkout in payments:
        checkout.process_payment()

transections = [
    StripePayment('TX901', 180000, "PKR"),
    PaypalPayment("TX902", 250.00, "ali@gmail.com"),
    EasypaisePayment("TX903", 15000, "+92-300-1234567") # if we don't use the "" double code in mobile number it would add then subtract and operations
]

checkout_all(transections)