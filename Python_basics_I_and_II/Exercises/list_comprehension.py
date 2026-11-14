# The old way of loop:
prices = [1800, 2500, 600]
discounted = []
for p in prices:
    discounted.append(p * 0.9)

print(discounted)

# The best of shortcut loop: 
prices1 = [1800, 2500, 600]
discounted1 = [p * 0.9 for p in prices1]

print(f"Comprehension Discount: {discounted1}")
# we can also filter in a good way possible: 
expensive = [p for p in prices if p > 1000]

print(expensive)

orders = [{'item': 'hoodie', 'price': 1800},
          {'item': 'cap', 'price': 600}]
prices2 = [o['price'] for o in orders]
big_orders = [o for o in orders if o['price'] > 1000]
print(prices2)

print(f"Big Orders: {big_orders}")

discount_dict = {p: p * 1.1 for p in prices}

print(discount_dict)

