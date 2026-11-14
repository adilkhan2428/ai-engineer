# Loop: Is a way to repeat one action multiple times  automatically.

# 1. Daily Sales Total - for loop basics
# sales = [1200, 2500, 1800, 900, 3200]

# for item in sales:
#     total = sum(sales)

# print(f"Total: ${total}")


# 2. Order Entry Until Stop - While loop
# total = 0
# count = 0

# while True:
#     x = input("Enter your product price (or 'done' to finish): ")
#     if x.lower() == 'done':
#         break
#     total += int(x)
#     count += 1
# print(f"Total bill: ${total} - Orders: {count}")

# 3. Stock Alert - enumerate + continue
# products = ["shirt", "hat", "jacket", "hoodie", "cap"]
# stocks =   [5,      0,     12,      0,       3]
# for index, (item, stock) in enumerate(zip(products, stocks), start=1):
#     if stock == 0:
#         continue
#     else:
#         print(f"{index}. {item} - {stock} left.")

# 4. BOSS - Fraud Order Detector
# orders = [1200, 2500, 800, 1800, 900, 99999]
# total = 0

# for order in orders:
#     if order == 99999:
#         print("Fraud detected! Stopping checkout")
#         break

#     if order < 1000:
#         print(f"Skipping small order: {order}")
#         continue

#     # Only valid orders reach here
#     total += order
#     print(f"Added: {order} | Running total: {total}")

# else:
#     # This else belongs to FOR, runs only if loop didn't break
#     print(f"All clear. Final Total: {total}")

# # If break happened, for-else won't run, so we still want to see this:
# if order == 99999:
#     print(f"Stopped. Safe total before fraud: {total}")

# Task: Login Retry Limit: 
# attempts = 0
# correct_password = "adil123"

# while True:
#     password = input("Enter password: ")
#     attempts += 1
#     if password == correct_password:
#         print(f"Login success after {attempts} attempt.")
#         break
#     if attempts == 3:
#         print("Account locked!")
#         break
#     else:
#         print(f"Wrong, {3 - attempts} tries left")
#         continue

# Loop: Is a way to repeat one action multiple times  automatically.

# 1. Daily Sales Total - for loop basics
# sales = [1200, 2500, 1800, 900, 3200]

# for item in sales:
#     total = sum(sales)

# print(f"Total: ${total}")


# 2. Order Entry Until Stop - While loop
# total = 0
# count = 0

# while True:
#     x = input("Enter your product price (or 'done' to finish): ")
#     if x.lower() == 'done':
#         break
#     total += int(x)
#     count += 1
# print(f"Total bill: ${total} - Orders: {count}")

# 3. Stock Alert - enumerate + continue
# products = ["shirt", "hat", "jacket", "hoodie", "cap"]
# stocks =   [5,      0,     12,      0,       3]
# for index, (item, stock) in enumerate(zip(products, stocks), start=1):
#     if stock == 0:
#         continue
#     else:
#         print(f"{index}. {item} - {stock} left.")

# 4. BOSS - Fraud Order Detector
# orders = [1200, 2500, 800, 1800, 900, 99999]
# total = 0

# for order in orders:
#     if order == 99999:
#         print("Fraud detected! Stopping checkout")
#         break

#     if order < 1000:
#         print(f"Skipping small order: {order}")
#         continue

#     # Only valid orders reach here
#     total += order
#     print(f"Added: {order} | Running total: {total}")

# else:
#     # This else belongs to FOR, runs only if loop didn't break
#     print(f"All clear. Final Total: {total}")

# # If break happened, for-else won't run, so we still want to see this:
# if order == 99999:
#     print(f"Stopped. Safe total before fraud: {total}")


# Task: Shop price entry with validation (while True + Continue)
# total = 0
# while True:
#     x = input("Enter product price (100 to 5000) or 'done': ")
#     if x.lower() == "done":
#         print(f"Total: ${total}")
#         break
#     price = int(x)
#     if price < 100 or price > 5000:
#         print("Invalid price, must be 100-5000")
#         continue
    
#     total += price
#     print(f"Added {price}, total now {total}")


