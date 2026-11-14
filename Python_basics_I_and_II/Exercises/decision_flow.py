# 1. Profit Margin Check Arithmetic + Comparison
# cost = 600
# selling = int(input("Enter selling price: "))
# profit = (selling - cost) / cost * 100

# if profit >= 50:
#     print(f"High profit {profit:.2f}% - Good!")
# elif profit >= 20:
#     print(f"OK profit {profit:.2f}%")
# else:
#     "Low profit - Increase price"

# 2. Bulk Order Validator - and, or, %(Modulus)
# quantity = int(input("Enter Quantity for Wholesale: "))
# if quantity > 10 and quantity < 100 and quantity % 5 == 0:
#     print("Wholesale approved!")
# else:
#     print("Must be 10-100 and mutiple of 5")

# 3. Coupen Code logic - in, not in, or
# 1. Define the variables first
# code = "save20"
# blacklisted_coupons = ["FRAUD50", "FAKE100"]
# valid_coupons = ["SAVE20", "WELCOME10"]

# # 2. Then run your logic
# if code.upper() in blacklisted_coupons:
#     print("Coupen blocked - fraud detected")
# elif code.upper() in valid_coupons:
#     print("Coupen applied")
# else:
#     print("Invalid coupen")

# BOSS - Adil Winter Checkout Engine:
product_price = int(input("Enter Product Price: "))
quantity =      int(input("Enter Quantity: "))
city =              input("Enter customer City: ")

subtotal = product_price * quantity
delivery = 100 if city.lower() == "Peshawar" else 250
total = subtotal + delivery
if product_price > 5000 and quantity >= 3:
    final_total = subtotal
    print(f"Free delivery! ${final_total}")
elif product_price > 3000:
    final_total = total * 0.9
    print(f"10% discount applied. ${final_total}")
else: 
    print(f"Final Total: ${total}")
    
