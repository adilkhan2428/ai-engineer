# # Dictionary: A data structure that store values: in (key, value) pair
# Batch 1: Creating & Accessing Dictionary - 3 Tasks

# # Task 1.1: Create your first Product 
# product = {
#     'name': "Winter Hoodie",
#     'price': 1800,
#     'stock': 15,
#     'city': "Peshawar"
# }
# print(product, '\n')
# cost = 1200
# # Task 1.2 - Access & Profit Calc
# print(product['name'], "\n")
# product["profit_percent"] = (product['price'] - cost) / cost * 100
# print(f"Price: {product['price']}, Profit: {product['profit_percent']:.2f}%,", "\n" )

# # Task 1.3 - Update & Add New Key
# product['stock'] = 12
# product["sold"] = 3
# product["category"] = "Winter"

# print(product)

# Batch 2: Dictionary Methods

# # Task 2.1 - Safe Access with .get()
# order = {"id": 101, "price": 2500}
# print(order["discount"]) # Crash the program:  KeyError: "discount"
# print(order.get("discount")) # No crash just: None
# print(order.get("discount", 0)) # return a default value i mean 0 if missing.

# # Task 2.2 - Loop with .items()
# product = {'name': "Winter Hoodie", 'price': 1800, 'stock': 12, 'sold': 3}
# for key, value in product.items():
#     print(f"{key} -> {value}")

# # Task 2.3 - Real Cleanup 
# order = {"id": 101, "product": "jacket", "price": 2500, "temp_key": "xyz", "city": "Lahore"}

# order.pop("temp_key")
# order.update({"status" : "paid", "delivery" : 100})

# print(order.keys(), '\n')
# print(order.values())

# Batch 3: Nested Dictionary 

# Task 3.1 - Create Nested dict
# order = {
#     'id': 205, 
#     'customer': {
#         'name': 'Usman',
#         'city': 'Lahore'
#     },
#     'item': {
#         'name': 'Jacket',
#         'price': 2500
#     }
# }

# # Task 3.2 - Deep Access 
# print(order['customer']['city'], '\n')
# print(order['item']['price'], '\n')
# total = order['item']['price'] * 2

# # Task 3.3 - Update Inside Nested
# order['customer']['city'] = 'Islamabad'
# order['item'].update({'discount': 200})
# order.update({'status': 'paid'})
# print(order)

# Batch 4 FINAL: List of Dictionaries - Real Adil Winter Daily Report 

# Task 4.1 - Loop Orders 
# daily_total = 0
# orders = [
#     {"id": 101, "product": "hoodie", "price": 1800, "qty": 2},
#     {"id": 102, "product": "jacket", "price": 2500, "qty": 1},
#     {"id": 103, "product": "cap", "price": 600, "qty": 3}
# ]
# orders.append({"id": 104, "product": "sample", "price": 0, "qty": 1})
# for order in orders:
#     total = order['price'] * order["qty"]
#     print(f"Order #{order['id']}: {order['product']} x {order['qty']} = {total}", '\n')
#     if order['price'] == 0:
#         continue
#     else:
#         daily_total += order["price"] * order["qty"]
# # Task 4.2 - Daily Total + Skip Free Samples
# print(f"Daily Total: {daily_total}")

# Task 4.3 - BOSS - Profit Filter + Nested Access
orders = [
    {"id": 101, "item": {"name": "hoodie", "price": 1800, "cost": 1200}, "qty": 2},
    {"id": 102, "item": {"name": "jacket", "price": 2500, "cost": 2000}, "qty": 1},
    {"id": 103, "item": {"name": "cap", "price": 600, "cost": 300}, "qty": 5}
]
for order in orders:
    profit_percent = (order['item']['price'] - order["item"]['cost'])/ order["item"]['cost'] * 100
    if profit_percent < 30:
        continue
    else:
        print(f"Order #{order['id']}: {order['item']['name']} {profit_percent:.2f}%")





