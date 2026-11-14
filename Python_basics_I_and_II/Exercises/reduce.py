# Reduce: This 'squashes' or compresses an entire list into one singl value (like a total sum) etc by prossing the item togathe or step by step.

from functools import reduce

prices = [1800, 600, 2500, 1200]

# 1. map: give 10% discount to each 
# Expected: [1620, 540, 2250, 1080]
discount = list(map(lambda p: p * 0.9, prices))

# 2. filter: keep only > 1000
# Expected: [1800, 2500, 1200]
big_order = list(filter(lambda b: b > 1000, prices))

# 3. reduce: find total sum 
# Expected: 6100
total_sum = reduce(lambda a, b: a + b, prices)

