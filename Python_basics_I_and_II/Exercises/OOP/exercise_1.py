# Task: Shopify discount & Tax engine
# Order processing for ecomerce store
class ShopifyOrder:
    store_currency = "USD"
    global_tax_rate = 0.08
    def __init__(self, order_id, customer_name, base_price, status='pending'):
        self.order_id = order_id
        self.customer_name = customer_name
        self.base_price = base_price
        self.status = status
    # instance method
    def update_status(self, status):
        self.status = status

# Instance Method: Works with a specific object, so it takes self as the first argument.

# Class Method: Works with the blueprint/class itself, so it takes cls as the first argument and must accept parameters if you want to update class variables dynamically.

    # class method 
    @classmethod
    def update_store_tax(cls, new_rate):
        cls.global_tax_rate = new_rate
    
    # static method
    @staticmethod
    def calculate_final_price(base_price, tax_rate):
        return base_price + (base_price * tax_rate)

# 1. Check initial class variables and create instances
print(f"Initial Tax Rate: {ShopifyOrder.global_tax_rate}")

order1 = ShopifyOrder("ORD-001", "Ali", 100.0)
order2 = ShopifyOrder("ORD-002", "Ahmad", 250.0)

# 2. Test instance method
order1.update_status("Paid")
print(f"Order 1 Status: {order1.status}")

# 3. Test static method (calculating final price using the class tax rate)
final_price_1 = ShopifyOrder.calculate_final_price(order1.base_price, ShopifyOrder.global_tax_rate)
print(f"Order 1 Final Price (with tax): {final_price_1}")

# 4. Test class method to update store-wide tax rate
ShopifyOrder.update_store_tax(0.10)
print(f"Updated Store Tax Rate: {ShopifyOrder.global_tax_rate}")

final_price_2 = ShopifyOrder.calculate_final_price(order2.base_price, ShopifyOrder.global_tax_rate)
print(f"Order 2 Final Price (with new tax): {final_price_2}")