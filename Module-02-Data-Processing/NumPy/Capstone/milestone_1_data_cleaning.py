"""
==================================================
NumPy Shopify Analytics Capstone
Milestone 1: Data Ingestion & Cleaning

Author: Adil Khan
Description:
This milestone simulates cleaning a raw Shopify
orders export before performing business analytics.
==================================================
"""

import numpy as np

# ==========================================
# Raw Shopify Orders Export
# ==========================================

orders = np.array([
    1200,
    np.nan,
    450,
    -50,
    780,
    0,
    np.nan,
    1500,
    230,
    999,
    -10,
    640,
    np.nan,
    85,
    420
], dtype=float)

# ==========================================
# Business Rules
# ==========================================
# NaN  -> Missing order value
# < 0  -> Corrupted order (remove)
# 0    -> Valid free replacement order (keep)

# ==========================================
# Step 1 — Inspect Raw Data
# ==========================================

print("=" * 50)
print("STEP 1 — RAW DATA INSPECTION")
print("=" * 50)

print(f"Shape               : {orders.shape}")
print(f"Data Type           : {orders.dtype}")
print(f"Missing Values      : {np.sum(np.isnan(orders))}")
print(f"Negative Values     : {np.sum(orders < 0)}")
print(f"Valid Orders        : {np.sum(orders >= 0)}")

# ==========================================
# Step 2 — Clean Data
# ==========================================

# Replace missing values with 0
clean_orders = np.nan_to_num(orders, nan=0)

# Remove corrupted orders
clean_orders = clean_orders[clean_orders >= 0]

print("\n" + "=" * 50)
print("STEP 2 — CLEANED DATA")
print("=" * 50)

print("Clean Orders:")
print(clean_orders)

print("\nOriginal Orders (Unchanged):")
print(orders)

# ==========================================
# Step 3 — Validate Cleaned Data
# ==========================================

print("\n" + "=" * 50)
print("STEP 3 — VALIDATION")
print("=" * 50)

print(f"Shape               : {clean_orders.shape}")
print(f"Total Orders        : {len(clean_orders)}")
print(f"Free Orders         : {np.sum(clean_orders == 0)}")
print(f"Minimum Order       : {np.min(clean_orders)}")
print(f"Maximum Order       : {np.max(clean_orders)}")