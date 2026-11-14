# map: This applies a specific rule or function to every item in a list and give you back a new list with the transformed values.

qtys = [2, 1, 3]  # old total = [3600, 1800, 5400]
totals = list(map(lambda q: q * 1800, qtys))

print(totals)

# We can also map othe function: if we already have some functions:
def discount(p):
    return p * 0.9
prices = [1200, 1800, 2500, 600]
discounted_prices  = list(map(discount, prices))

print(discounted_prices)


