import numpy as np


# Optimze version of exercises: TASKS:
# 1. Convert the Price from list to NumPy Array.
# 2. Shopify Bulk Currency Converter
def get_sale_prices(prices_np):
    # Pure logic:
    return prices_np * 0.85


# Logic for Currency Conversion
def pkr_to_usd_agent(prices_np, conversion_rate):
    # Pure logic: vectorized operation only
    return prices_np / conversion_rate


# --- ENTRY POINT (Data enters the system here) ---
raw_prices = [4599, 5000, 3400, 2000, 1200]

# CAST ONCE: This is the senior habit
prices_np = np.array(raw_prices)

# Pass the high-performance object to the logic functions
sale_output = get_sale_prices(prices_np)
usd_output = pkr_to_usd_agent(prices_np, 280)

print(f"Sale Prices: {sale_output}")
print(f"USD Prices: {usd_output}")
