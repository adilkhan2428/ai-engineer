# Function: Is a reusable block of code. 
# Use for Reusability, and modularity in code. 

# Batch 1: Creating & Calling Functions — FAST MODE (3 Tasks)

# Task 1.1 - First Function
# def print_header():
#     print("=== Adil Winter Store ===")
#     print("Peshawar")

# print_header()
# Task 1.2 - Greet Customer 
# def greet_customer(name):
#     print(f"Welcome, {name}! to Adil Winter")
# greet_customer("Safi Khan")

# Task 1.3 - Product Display 
# def show_product(name, price):
#     print(f"Product: {name} | Price: {price}")

# show_product("Hoodie", 1800)
# show_product("Jacket", 2500)

# Batch 2: Parameters + Profit Logic — FAST MODE (3 Tasks)

# 
# Batch 2: Parameters + Profit Logic — FAST MODE (3 Tasks)

# Task 2.1 - Total Calculator 
# def calculate_total(price, qty):
#     total = price * qty
#     print(f"Total: {total}")
# calculate_total(1800, 2)
# calculate_total(2500, 3)

# # Task 2.2 - Profit Calculator 
# def calculate_profit(price, cost):
#     profit = price - cost
#     percent = (price - cost)/cost * 100
#     print(f"Profit: {profit} | Profit %: {percent:.2f}%")
# calculate_profit(1800, 1200)

# # Task 2.3 - Checkout Line
# def checkout_line(product, price, qty):
#     total = price * qty
#     print(f"{product} x {qty} =  {total}")
# checkout_line("Hoodie", 1800, 2)

# Batch 3: Return vs Print - EXPLAIN THEN TASKS
# print = just show on screen, value disappears.
# return = give value back, so you can store and use later.

# Task 3.1 - Return vs Print 
# def get_total(price, qty):
#     return price * qty

# result = get_total(1800, 2)
# print(result)
# print(f"Daily: {result + 100}") # Prove we can use it, add delivery

# # Task 3.2 - Return Profit %
# def get_profit_percent(price, cost):
#     return (price - cost)/cost * 100

# p = get_profit_percent(1800, 1200)
# if p > 40:
#     print(f"High profit: {p} - Push ads!")

# # Task 3.3 - Return Dictionary (very important)
# def create_product(name, price, cost):
#     return {"name": name, "price": price, "profit": price - cost}
# prod = create_product("Hoodie", 1800, 1200)

# print(prod)
# print(prod['profit'])

# Batch 4: Default Parameters — Assessment Mode (3 Tasks)
# Task 4.1 - Default City
# 

# Batch 5: Functions + Dictionary + Loops — Your Real Work

# Task 5.1 - Single Order Total (Dict in Function)
def get_total_from_order(order_dict):
    return order_dict["price"] * order_dict["qty"]

order = {"id": 101, "product": "hoodie", "price": 1800, "qty": 2}
print(get_total_from_order(order))

# Task 5.2 - Daily Total (Loop INSIDE Function)
# def get_daily_total(orders_list):
#     total = 0
#     for order in orders_list:
#         if order['price'] == 0:
#             continue
#         total += order['price'] * order['qty']
#     return total

# orders = [
#     {"id": 1, "product": "Hoodie", "price": 1800,"cost": 1200, "qty": 2},
#     {"id": 2, "product": "Jacket", "price": 2500,"cost": 2200, "qty": 1},
#     {"id": 3, "product": "Sample", "price": 2, "cost": 1, "qty": 1}
# ]

# print(get_daily_total(orders))

# # Task 5.3 - Profit Filter Function:
# def get_high_profit_orders(orders):
#     high = []
#     for order in orders:
#         profit = (order["price"] - order['cost'])/ order['cost'] * 100
#         if profit >= 30:
#             high.append(order)
#     return high

# print(get_high_profit_orders(orders))

# Batch 6: Final Boss - Report Automation (The Real Store System)

# Task 6.1 - Helper Function 
def calculate_profit_percent(price, cost):
    return (price - cost)/ cost * 100
# Task 6.2 - Single Order Report (Calls 6.1)
def order_report(order):
    if order['price'] == 0:
        return "skip"
    total = order["price"] * order["qty"]
    percent = calculate_profit_percent(order['price'], order['cost'])
    print(f"Order {order['id']}: {order['product']} | Qty: {order['qty']} | Total: {total} | Profit %: {percent:.2f}")

# TEST ORDERS - Your Adil Winter Store Data
orders = [
    {"id": 101, "product": "Wool Hoodie", "price": 1800, "cost": 1200, "qty": 2},
    {"id": 102, "product": "Winter Jacket", "price": 3500, "cost": 2800, "qty": 1},
    {"id": 103, "product": "Beanie Cap", "price": 600, "cost": 350, "qty": 3},
    {"id": 104, "product": "Sample", "price": 0, "cost": 0, "qty": 1}
]

# Expected:
# 101: Total 3600, Profit% 50.0%
# 102: Total 3500, Profit% 25.0%
# 103: Total 1800, Profit% 71.4%
# 104: Sample - should be skipped with continue
# Grand Total = 3600+3500+1800 = 8900

# Task 6.3 - DAILY REPORT AUTOMATION (Final Test)
def daily_sales_report(orders_list):
    grand_total = 0
    for order in orders_list:
        if order['price'] == 0:
            continue
        order_report(order)
        grand_total += order['price'] * order['qty']
    print(f"==== Grand Total: {grand_total} ====")

daily_sales_report(orders)