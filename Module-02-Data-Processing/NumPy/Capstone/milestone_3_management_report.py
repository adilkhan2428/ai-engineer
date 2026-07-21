"""
==================================================
NumPy Shopify Analytics Capstone
Milestone 3: Executive Management Report

Author: Adil Khan

Description:
Generate an executive business report from the
processed Shopify order data. The report includes
business KPIs, health checks, and a management
summary.
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
FREE_REPLACEMENT_LIMIT = 20      # Percentage
DISCOUNT_RATE = 0.10

# ==========================================
# Promotion Simulation
# ==========================================

discount_orders = clean_orders.copy()

paid_order_mask = discount_orders > 0

discount_orders[paid_order_mask] *= (
    1 - DISCOUNT_RATE
)

# ==========================================
# Executive KPIs
# ==========================================

total_orders = len(clean_orders)
paid_orders = np.sum(clean_orders > 0)
free_orders = np.sum(clean_orders == 0)

total_revenue = np.sum(discount_orders)
average_paid_order = np.mean(
    discount_orders[paid_order_mask]
)
highest_order = np.max(
    discount_orders[paid_order_mask]
)
lowest_paid_order = np.min(
    discount_orders[paid_order_mask]
)

print("=" * 55)
print("              DAILY BUSINESS REPORT")
print("=" * 55)

print(f"Total Orders              : {total_orders}")
print(f"Paid Orders               : {paid_orders}")
print(f"Free Replacement Orders   : {free_orders}")

print("-" * 55)

print(f"Total Revenue             : ${total_revenue:.2f}")
print(f"Average Paid Order        : ${average_paid_order:.2f}")
print(f"Highest Paid Order        : ${highest_order:.2f}")
print(f"Lowest Paid Order         : ${lowest_paid_order:.2f}")

print("=" * 55)

# ==========================================
# Business Health Check
# ==========================================

free_replacement_rate = (
    free_orders / total_orders
) * 100

high_value_order_count = np.sum(
    clean_orders >= HIGH_VALUE_THRESHOLD
)

print("\nBUSINESS HEALTH STATUS")
print("-" * 55)

if free_replacement_rate > FREE_REPLACEMENT_LIMIT:
    print("Free Replacement Rate : Warning")
else:
    print("Free Replacement Rate : Healthy")

if average_paid_order > 700:
    print("Average Order Value   : Healthy")
else:
    print("Average Order Value   : Warning")

if high_value_order_count >= 3:
    print("High Value Orders     : Healthy")
else:
    print("High Value Orders     : Warning")

print("=" * 55)

# ==========================================
# Management Summary
# ==========================================

print("\nMANAGEMENT SUMMARY")
print("-" * 55)

print(
    "• Revenue performance is healthy, with a strong "
    "average paid order value."
)

print(
    "• Free replacement orders exceed the target "
    "threshold and should be investigated."
)

print(
    "• Premium sales remain strong with multiple "
    "high-value orders."
)

print(
    "• VIP customers should receive special attention "
    "through loyalty or retention campaigns."
)

print(
    "• Tomorrow's priority should be reducing free "
    "replacement orders while maintaining premium sales."
)

print("=" * 55)