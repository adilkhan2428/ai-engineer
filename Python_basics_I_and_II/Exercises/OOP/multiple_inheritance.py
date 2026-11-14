# Multiple Inheritance
# Definition: A single child class inheriting directly from two or more separate parent classes at the same time.

# Key Characteristic: Combines separate, independent capabilities/responsibilities into one unified child class without duplicating code.

# Example Structure:

class InventoryTracking:
    def check_stock(self):
        print("Checking product stock...")
class PaymentProcessing:
    def process_payment(self):
        print("Processing customer payment...")
class ShopifyStore(InventoryTracking, PaymentProcessing):
    def manage_orders(self):
        print("Managing Shopify orders...")

store = ShopifyStore()

store.check_stock()
store.process_payment()
store.manage_orders()

# One distinction to remember: Multiple inheritance combines capabilities from multiple parents. It does not mean that the child owns independent copies of their methods.