# variables are the fundamentals concepts of any programming language. 
# variable: is the word that store values in memory that can be change any time. (OR)
# Variable is simply a name that point to some data in memory. 
name = "Adil khan" # this is string or text. 
education = "Fsc" 
age = 20  # this is integar it store numeric data.
country = "Pakistan"
muslim = True # this is boolean it store the decision type or just binary data, True --> (1) --> Yes and False --> (0) --> No

# Rules for variables names: 
# i) Must start with a letter or underscore.
# i) Cannot start with a number -->  2_brother = "brother1 and brother2" --> this is wrong
# iii) Can contain only letter, number and (_) underscore. 
# Python keywords are not allowed. like: class = "10th" --> Wrong and other like: for, if, else, return, void, def, init, pip etc.
print(name)
print(age)
print(country)
print(muslim)
# Shirt price calculator - int casting
#shirt_quantity = int(input("Enter your Shirts Quantity: "))
price = 1200
#total = price * shirt_quantity
#print(total)

# Discount Check: 
#original_price = float(input("Enter original price: "))
#price_discount = float(input("Enter discount %: "))
#final_price = original_price - price_discount 
#print(final_price)

# Order ID Fixer: String vs int trap

order_id = 101
user_input = input("Enter last 2 digit to add: ")

print(type(str(order_id) + user_input))
print()
print(str(order_id) + user_input)

# BOSS - Daily Sales Report with Type Check
sales_str = input("Enter today's sales separated by comma: ")
parts  = sales_str.split(",")
list = [int(p.strip()) for p in parts]

total_sales = sum(list)
avg_sales = sum(list) / len(list)

print(f"Total Sales: {total_sales}")
print(f"Average: {avg_sales:.2f}")


