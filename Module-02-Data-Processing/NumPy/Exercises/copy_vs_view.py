# Exercise to demonstrate how View vs Copy works
# A Shopify store exported product prices.
import numpy as np
prices = np.array([120, 450, 980, 150, 60, 720])
last_four_prices = prices[2:].copy() # .astype(np.float32) # --> if we want to run the program.
# here if we didn't use .copy() so, the discount apply as well on all prices and the prices array will change.
last_four_prices *= 0.9
print("Discounted Last four prices: ")
print(last_four_prices)
print("\nThe Orginal Prices Array: ")
print(prices)