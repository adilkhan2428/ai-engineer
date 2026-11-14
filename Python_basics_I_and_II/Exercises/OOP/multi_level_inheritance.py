## 3. Multi-Level Inheritance
# Definition: An inheritance chain that passes across **multiple generations** of classes (`Grandparent` --> `Parent` --> `Child`).
# Key Characteristic: The bottom child class gets direct access to **all** methods and attributes defined across every single level above it.
# Example Structure:

# class Order:  # Level 1 (Grandparent)
#     pass


# class OnlineOrder(Order):  # Level 2 (Parent)
#     pass


# class ExpressPhysicalOrder(OnlineOrder):  # Level 3 (Child)
#       pass

# # Level 1: Grandparent Class (Base Order)
# class Order:
#     def __init__(self, order_id, customer, amount):
#         self.order_id = order_id
#         self.customer = customer
#         self.amount = amount

#     def display_order(self):
#         print(f"Order ID: {self.order_id}")
#         print(f"Customer: {self.customer}")
#         print(f"Amount: ${self.amount}")


# # Level 2: Parent Class (Inherits from Order)
# class OnlineOrder(Order):
#     def __init__(self, order_id, customer, amount, platform):
#         super().__init__(order_id, customer, amount)  # Reuses Order constructor
#         self.platform = platform

#     def track_sync(self):
#         print(f"Syncing order {self.order_id} with {self.platform} API...")


# # Level 3: Child Class (Inherits from OnlineOrder)
# class ExpressPhysicalOrder(OnlineOrder):
#     def __init__(self, order_id, customer, amount, platform, courier_service):
#         super().__init__(order_id, customer, amount, platform)  # Reuses OnlineOrder constructor
#         self.courier_service = courier_service

#     def dispatch_express(self):
#         print(f"Dispatching express package via {self.courier_service}!")


# # --- Testing the Multilevel Chain ---

# # Creating an instance of the bottom child class
# express_order = ExpressPhysicalOrder(
#     order_id=5001, 
#     customer="Adil", 
#     amount=12000, 
#     platform="Shopify", 
#     courier_service="TCS Express"
# )

# # Calling methods from ALL THREE levels:
# print("--- 1. Base Order Method ---")
# express_order.display_order()         # Inherited from Order (Grandparent)

# print("\n--- 2. Intermediate OnlineOrder Method ---")
# express_order.track_sync()            # Inherited from OnlineOrder (Parent)

# print("\n--- 3. Specific ExpressPhysicalOrder Method ---")
# express_order.dispatch_express()      # Defined in ExpressPhysicalOrder (Child)

# Task ecommerce exerise:
class Business:
    def __init__(self, business_name, owner, location):
        self.business_name = business_name
        self.owner = owner
        self.location = location
    def business_info(self):
        print(f"Business Name: {self.business_name} Owner: {self.owner} Location: {self.location}")

class EcommerceBusiness(Business):
    def sell_online(self):
        print(f"{self.business_name} sells products online.")
class ShopifyStore(EcommerceBusiness):
    def manage_shopify_orders(self):
        print(f"{self.business_name} manages orders through Shopify")

store1 = ShopifyStore("Adil Winter", "Safi", "new york")
store1.business_info()
store1.sell_online()
store1.manage_shopify_orders()