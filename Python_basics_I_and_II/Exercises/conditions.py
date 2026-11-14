# Exercises
# 1. Winter Stock Check - Simple if / else
# stock = 10
# user_input = int(input("How many Shirts you want to buy? "))

# if user_input <= stock:
#     print("Order Confirmed")
# else:
#     print("Only 10 Left! ")

# # 2. Delivery Charge - if/elif/else
# city = input("Enter your city: ")

# delivery_charge = 0

# if city.lower() == "peshawar":
#     delivery_charge = 100
#     print(delivery_charge)
# elif city.lower() == "karachi" or city.lower() == "lahore":
#     delivery_charge = 250
#     print(delivery_charge)
# else:
#     delivery_charge = 400
#     print(delivery_charge)

# # 3. Nested Conditions 

# total = int(input("Enter your Total spent so far: "))
# is_member = input("Are you member? (yes/no): ")

# if total > 5000:
#     if is_member.lower() == "yes":
#         total = total * (1 - 0.25)
#         print("VIP Gold - 25% off next order")
#         print(f"Total: ${total}")
#     else:
#         total = total * (1 -0.15) 
#         print("VIP silver - 15% off , become member for 25%")
#         print(f"Total: ${total}")
# else:
#     print("Regular customer - spend 5000 for VIP")
#     print(f"Total: ${total}")


