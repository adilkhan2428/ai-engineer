# RECURSION: Function calling itself, but with smaller problem. 
# 2 Rules: 1. Base Case - Stop Condition: othewise infinite loop and laptop hangs. 
#  2. Recursive Case - Call itself with smaller number. 

# Sample Recursive function example:
# def countdown(n):
#     # Rule 1: Base case - when  to stop 
#     if n == 0:
#         print('done!')
#         return

#     # Rule 2. Recursive case - do work + call smaller 
#     print(n)
#     countdown(n-1) # same function but n is smaller each time, until it reach rule 1

# countdown(15)

# # Task on Recursion: 
# def print_hoodies(n):
#     if n ==  0:
#         print("Stock finished!")
#         return
#     print(f"Hoodie quantity remaining: {n}")
#     print_hoodies(n - 1)

# print_hoodies(5)

# # Task  Total of prices with Recursion
def total_recursive(prices):
    if len(prices) == 0:
        return 0
    return prices[0] + total_recursive(prices[1:])

# Test
prices = [1800, 600, 2500]
# print(total_recursive(prices))
print(prices[1])

# # Task: Printing Count of orders 
# def count_orders(orders):
#     if len(orders) == 0:
#         return 0
#     return 1 + count_orders(orders[1:])

# print(count_orders([1,2,3,4]))
# print(count_orders([1800, 2500]))

