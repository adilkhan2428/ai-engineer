class CartItem:
    """Standard cart item with base tax rules"""
    tax_rate = 0.05  # 5% standard tax

    def __init__(self, name, base_price, quantity):
        self.name = name
        self.base_price = base_price
        self.quantity = quantity

    def get_subtotal(self):
        return self.base_price * self.quantity

    def calculate_final_price(self):
        # Base implementation: subtotal + standard tax
        subtotal = self.get_subtotal()
        return subtotal * (1 + self.tax_rate)

    def get_item_summary(self):
        final = self.calculate_final_price()
        return f"[Standard] {self.name} (Qty: {self.quantity}) — Final: PKR {final:,.2f}"


class FlashSaleItem(CartItem):
    """Applies a timed promotional discount before tax"""

    def __init__(self, name, base_price, quantity, discount_percentage):
        super().__init__(name, base_price, quantity)
        self.discount_percentage = discount_percentage  # e.g., 15 for 15%

    def calculate_final_price(self):  # OVERRIDING parent method
        subtotal = self.get_subtotal()
        discounted_amount = subtotal * (1 - (self.discount_percentage / 100))
        return discounted_amount * (1 + self.tax_rate)

    def get_item_summary(self):
        final = self.calculate_final_price()
        return f"[Flash Sale {self.discount_percentage}%] {self.name} (Qty: {self.quantity}) — Final: PKR {final:,.2f}"


class B2BWholesaleItem(CartItem):
    """Applies high-volume tier discounts and tax exemptions"""

    def __init__(self, name, base_price, quantity, bulk_threshold=10, bulk_discount=0.25):
        super().__init__(name, base_price, quantity)
        self.bulk_threshold = bulk_threshold
        self.bulk_discount = bulk_discount  # e.g., 25% off for bulk

    def calculate_final_price(self):  # OVERRIDING parent method
        subtotal = self.get_subtotal()
        if self.quantity >= self.bulk_threshold:
            # Apply bulk discount and 0% tax for wholesale
            return subtotal * (1 - self.bulk_discount)
        else:
            # Fall back to standard pricing if below threshold
            return subtotal * (1 + self.tax_rate)

    def get_item_summary(self):
        final = self.calculate_final_price()
        status = "Bulk Applied" if self.quantity >= self.bulk_threshold else "Standard B2B"
        return f"[B2B Wholesale - {status}] {self.name} (Qty: {self.quantity}) — Final: PKR {final:,.2f}"


# ── Polymorphic Checkout Pipeline ─────────────────────────
def process_checkout(cart_items):
    print("=== E-COMMERCE CHECKOUT REPORT ===")
    grand_total = 0.0
    for item in cart_items:
        # Polymorphism in action: Python resolves the correct overridden calculate_final_price()
        print(item.get_item_summary())
        grand_total += item.calculate_final_price()
    
    print("-" * 40)
    print(f"GRAND TOTAL: PKR {grand_total:,.2f}\n")


# ── Test Execution ────────────────────────────────────────
cart = [
    CartItem("Generic Phone Case", 1500, 2),
    FlashSaleItem("Wireless Earbuds", 8000, 1, discount_percentage=20),
    B2BWholesaleItem("Shopify Printer Labels (Rolls)", 500, 15, bulk_threshold=10, bulk_discount=0.30)
]

process_checkout(cart)