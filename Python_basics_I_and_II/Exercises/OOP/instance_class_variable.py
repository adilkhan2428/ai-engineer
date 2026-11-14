# # Instance variable: are variable tht belong to an individual object (instance) of a class, each object maintains its own values, independent of other objects.
# class Order:
#     def __init__(self, customer, amount):
#         self.customer = customer  # instance variable
#         self.amount = amount      # instance variable


# order_1 = Order("Adil", 7500) # order_1 and order_2 have their own independent values.
# order_2 = Order("Ahmad", 8000)

# print("Order 1:",order_1.customer, order_1.amount)
# print("Order 2:", order_2.customer, order_2.amount)


# # Class Variables: are variables defined directly inside a class, outside its methods. They belong to the class and are shared by its instances unless an instance creates its own attributes with the same name.
# class Order:
#     store_name = "Adil's Fashion Store" # store_name is a class variable
#     # it is defined directly inside the class.

#     def __init__(self, customer, amount):
#         self.customer = customer
#         self.amount = amount

# order1 = Order("Ali", 4000)
# order2 = Order("Ahmad", 6000)
# order1.store_name = "New store"
# print(order1.store_name)
# print(order2.store_name)
# print(Order.store_name)


# COMBINE EXAMPLE of shopify:

class Order:
    # class variable
    storename = "Adil's winter shop"

    def __init__(self, customer, amount, payment_status):
        # instance variable
        self.customer = customer
        self.amount = amount
        self.payment_status = payment_status

    def show_order(self):
        print("Store:", self.storename)
        print("Customer:", self.customer)
        print("Amount:", self.amount)
        print("Payment:", self.payment_status)

order_one = Order("Behram", 1500, "Paid")
order_two = Order("Ahmad", 1200, "Pending")

order_one.show_order()
print("--------------")
order_two.show_order()


# Python built-in attributes
print(order_one.__dict__)