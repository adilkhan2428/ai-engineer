"""
==================================================
NumPy Shopify Analytics Capstone
Milestone 2: Business Analytics

Author: Adil Khan

Description:
This milestone analyzes cleaned Shopify order data
to generate business KPIs and simulate a marketing
promotion using NumPy.
==================================================
"""

import numpy as np

# ==========================================
# Clean Shopify Orders Dataset
# ==========================================

clean_orders = np.array([
    1200., 0., 450., 780., 0., 0.,
    1500., 230., 999., 640., 0.,
    85., 420.
])

# ==========================================
# Business Rules
# ==========================================

HIGH_VALUE_THRESHOLD = 800
DISCOUNT_RATE = 0.10

# ==========================================
# Part 1 — Revenue Metrics
# ==========================================

total_revenue = np.sum(clean_orders)
average_order_value = np.mean(clean_orders)
highest_order = np.max(clean_orders)
lowest_order = np.min(clean_orders)

print("=" * 55)
print("PART 1 — REVENUE METRICS")
print("=" * 55)

print(f"Total Revenue         : ${total_revenue:.2f}")
print(f"Average Order Value   : ${average_order_value:.2f}")
print(f"Highest Order         : ${highest_order:.2f}")
print(f"Lowest Order          : ${lowest_order:.2f}")

# ==========================================
# Part 2 — High-Value Orders
# ==========================================

high_value_orders = clean_orders[
    clean_orders >= HIGH_VALUE_THRESHOLD
]

high_value_percentage = (
    len(high_value_orders) / len(clean_orders)
) * 100

print("\n" + "=" * 55)
print("PART 2 — HIGH-VALUE ORDERS")
print("=" * 55)

print(f"Threshold             : ${HIGH_VALUE_THRESHOLD}")
print(f"Number of Orders      : {len(high_value_orders)}")
print(f"Order Values          : {high_value_orders}")
print(f"Percentage            : {high_value_percentage:.2f}%")

# ==========================================
# Part 3 — Customer Segments
# ==========================================

small_orders = clean_orders[
    clean_orders < 300
]

medium_orders = clean_orders[
    (clean_orders >= 300) &
    (clean_orders <= 799)
]

large_orders = clean_orders[
    clean_orders >= HIGH_VALUE_THRESHOLD
]

print("\n" + "=" * 55)
print("PART 3 — ORDER SEGMENTS")
print("=" * 55)

print(f"Small Orders (<300)        : {len(small_orders)}")
print(f"Medium Orders (300-799)    : {len(medium_orders)}")
print(f"Large Orders (>=800)       : {len(large_orders)}")

# ==========================================
# Part 4 — Promotion Simulation
# ==========================================

discount_orders = clean_orders.copy()

paid_order_mask = discount_orders > 0

discount_orders[paid_order_mask] *= (
    1 - DISCOUNT_RATE
)

discounted_revenue = np.sum(discount_orders)

revenue_lost = (
    total_revenue - discounted_revenue
)

print("\n" + "=" * 55)
print("PART 4 — PROMOTION SIMULATION")
print("=" * 55)

print(f"Discount Rate        : {DISCOUNT_RATE * 100:.0f}%")
print(f"Revenue After Sale   : ${discounted_revenue:.2f}")
print(f"Revenue Lost         : ${revenue_lost:.2f}")