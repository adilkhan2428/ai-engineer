# Scope = access: where and how much scope or access the variable carry. 
# 1.  Local variable: A variable that defined inside a function and can be used inside that function. we can't use it outside of function.
# 2. Global varialbe: A varialbe that defined outside a function and can be used both inside and outside of the function. 
# it is recommended: that 90% of the function should be local in -- production

# current_balance = 40000
# def withdraw(amount):
#     global current_balance # tell python: use the outside one
#     current_balance = current_balance - amount 
#     return current_balance

# print(withdraw(15000))

# Task: 
# GLOBAL
# shop_name = "Zaman Hoodies"

# def show_shop():
#     # print shop_name (should work - reading global)
#     print(shop_name)

# def change_shop():
#     shop_name = "New_Hoodie" # LOCAL - different variable
#     print(shop_name)

# # Write the two functions

# show_shop()
# change_shop()
# print(shop_name) # This will print --> "Zaman Hoodies"


# Exercise: 1 The coupen budget Tracker
wallet_balance = 100
def apply_coupen(discount):
    global wallet_balance 
    wallet_balance -= discount

apply_coupen(20)

print(wallet_balance)

# Exercise: 2 The Secret API Key 
# def initialize_app():
#     api_key = "secret_12345"
#     print("App initialized successfully!")

# # 1. Call the function here
# print(initialize_app())

# # 2. Try to print the local variable here and observe the error
# print(api_key) # it give us the NameError: name 'api_key' is not defined
