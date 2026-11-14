# pass  # is a plceholder. it tells python that the class body is intentionally empty for now.


class Order:
    def __init__(self, order_id, customer_name, total_amount):
        # Attributes: The state/data belonging to a specific order
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount
        self.payment_status = "Pending"
    
    # Methods: The behavior/actions an order can perform on its own data
    def apply_discount(self, discount_amount):
        if discount_amount > self.total_amount:
            print(f"Error: Discount exceeds total for Order #{self.order_id}")
            return
        self.total_amount -= discount_amount
        print(f"Applied ${discount_amount} discount to Order #{self.order_id}. New total: ${self.total_amount}")

    def confirm_payment(self):
        self.payment_status = "Paid"
        print(f"Payment confirmed for Order #{self.order_id}. Status is now: {self.payment_status}")

    def get_order_summary(self):
        return f"Order #{self.order_id} | Customer: {self.customer_name} | Total: ${self.total_amount} | Status: {self.payment_status}"


# --- Real-World Usage ---

# 1. Creating independent instances (objects) from our blueprint (class)
order_101 = Order(101, "Aiden Vance", 150.00)
order_102 = Order(102, "Sara Connor", 320.50)

# 2. Interacting with their individual behaviors and states
print(order_101.get_order_summary())
# Output: Order #101 | Customer: Aiden Vance | Total: $150.0 | Status: Pending

print("-" * 40)

# Apply a discount and confirm payment for order_101 only
order_101.apply_discount(25.00)
order_101.confirm_payment()

print("-" * 40)

# Notice how order_102 remains completely untouched and independent
print(order_101.get_order_summary())
print(order_102.get_order_summary())