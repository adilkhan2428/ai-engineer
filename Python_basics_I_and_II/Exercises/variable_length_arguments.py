# Variable Length arguments (*args): This allow a function to accept any number of inputs, inside the function, these multiple values bundled togather, and are treated as tuple.

# def total_sales(*prices):
#     sum = 0
#     for p in prices:
#         sum += p
#     return sum 

# bill = total_sales(1800, 2500)
# bill2 = total_sales(1800, 2500, 600, 800, 800)

# print(bill)
# print()
# print(bill2)

# Task: Make function that takes any number of quantities for hoodie (price 1800 each) and returns total bill.
def bill_hoodie(*qtys):
    price = 1800
    total = price * sum(qtys)
    return total

print(bill_hoodie(2)) # 3600
print(bill_hoodie(2,1,3)) # (2+1+3)*1800 = 10800