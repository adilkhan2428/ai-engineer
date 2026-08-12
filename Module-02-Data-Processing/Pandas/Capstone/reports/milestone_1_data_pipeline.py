import pandas as pd
import numpy as np


# ============================================================
# MILESTONE 1 — DATA PIPELINE
# ============================================================

# ------------------------------------------------------------
# 1. Load Raw Data
# ------------------------------------------------------------

orders = pd.read_csv("Module-02-Data-Processing\\Pandas\\Capstone\\data\\orders.csv")
products = pd.read_csv("Module-02-Data-Processing\\Pandas\\Capstone\\data\\products.csv")

print("Orders shape:", orders.shape)
print("Products shape:", products.shape)

print("\nOrders:")
print(orders.head())

print("\nProducts:")
print(products.head())


# ------------------------------------------------------------
# 2. Initial Data Inspection
# ------------------------------------------------------------

print("\nOrders information:")
orders.info()

print("\nMissing values:")
print(orders.isna().sum())

print("\nDuplicate Order IDs:")
print(orders["Order ID"].duplicated().sum())


# ------------------------------------------------------------
# 3. Clean Orders
# ------------------------------------------------------------

completed_orders = orders.copy()

# Convert date
completed_orders["Order Date"] = pd.to_datetime(
    completed_orders["Order Date"],
    errors="coerce"
)

# Clean text columns
text_columns = [
    "Order Status",
    "Payment Method",
    "Customer Name",
    "Region",
    "Customer Segment"
]

for column in text_columns:
    completed_orders[column] = (
        completed_orders[column]
        .astype("string")
        .str.strip()
    )


# Convert numeric columns
numeric_columns = [
    "Order ID",
    "Customer ID",
    "Product ID",
    "Units Sold",
    "Revenue"
]

for column in numeric_columns:
    completed_orders[column] = pd.to_numeric(
        completed_orders[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4. Keep Completed Orders
# ------------------------------------------------------------

completed_orders = completed_orders.query(
    "`Order Status` == 'Completed'"
).copy()

print("\nCompleted orders:", len(completed_orders))


# ------------------------------------------------------------
# 5. Validate Basic Business Data
# ------------------------------------------------------------

# Units sold must be positive
completed_orders.loc[
    completed_orders["Units Sold"] <= 0,
    "Units Sold"
] = np.nan

# Revenue cannot be negative
completed_orders.loc[
    completed_orders["Revenue"] < 0,
    "Revenue"
] = np.nan


# ------------------------------------------------------------
# 6. Clean Product Master
# ------------------------------------------------------------

products["Product Name"] = (
    products["Product Name"]
    .astype("string")
    .str.strip()
)

products["Category"] = (
    products["Category"]
    .astype("string")
    .str.strip()
)

products["Unit Cost"] = pd.to_numeric(
    products["Unit Cost"],
    errors="coerce"
)


# ------------------------------------------------------------
# 7. Merge Orders with Product Master
# ------------------------------------------------------------

completed_orders = completed_orders.merge(
    products[
        [
            "Product ID",
            "Product Name",
            "Category",
            "Unit Cost"
        ]
    ],
    on="Product ID",
    how="left",
    validate="many_to_one"
)


# ------------------------------------------------------------
# 8. Detect Unmatched Products
# ------------------------------------------------------------

unmatched_products = completed_orders[
    completed_orders["Product Name"].isna()
]

print("\nUnmatched product records:")
print(
    unmatched_products[
        ["Order ID", "Product ID", "Revenue"]
    ]
)

print(
    "\nNumber of unmatched product records:",
    len(unmatched_products)
)


# ------------------------------------------------------------
# 9. Financial Feature Engineering
# ------------------------------------------------------------

completed_orders["Total Cost"] = (
    completed_orders["Units Sold"]
    * completed_orders["Unit Cost"]
)

completed_orders["Profit"] = (
    completed_orders["Revenue"]
    - completed_orders["Total Cost"]
)

completed_orders["Profit Margin %"] = (
    completed_orders["Profit"]
    / completed_orders["Revenue"]
    * 100
)


# ------------------------------------------------------------
# 10. Time Features
# ------------------------------------------------------------

completed_orders["Year"] = (
    completed_orders["Order Date"].dt.year
)

completed_orders["Month"] = (
    completed_orders["Order Date"].dt.month
)

completed_orders["Month Name"] = (
    completed_orders["Order Date"].dt.strftime("%B")
)

completed_orders["Day of Week"] = (
    completed_orders["Order Date"].dt.day_name()
)


# ------------------------------------------------------------
# 11. Customer Contribution Using transform()
# ------------------------------------------------------------

completed_orders["Customer Total Revenue"] = (
    completed_orders
    .groupby("Customer ID")["Revenue"]
    .transform("sum")
)

completed_orders["Order Contribution %"] = (
    completed_orders["Revenue"]
    / completed_orders["Customer Total Revenue"]
    * 100
)


# ------------------------------------------------------------
# 12. Segment Contribution Using transform()
# ------------------------------------------------------------

completed_orders["Segment Total Revenue"] = (
    completed_orders
    .groupby("Customer Segment")["Revenue"]
    .transform("sum")
)

completed_orders["Segment Revenue Share %"] = (
    completed_orders["Segment Total Revenue"]
    / completed_orders["Revenue"].sum()
    * 100
)


# ------------------------------------------------------------
# 13. Data Quality Summary
# ------------------------------------------------------------

print("\n================ DATA QUALITY ================")

print(
    "Total raw orders:",
    len(orders)
)

print(
    "Completed orders:",
    len(completed_orders)
)

print(
    "Duplicate Order IDs:",
    completed_orders["Order ID"].duplicated().sum()
)

print(
    "Missing Order Dates:",
    completed_orders["Order Date"].isna().sum()
)

print(
    "Unmatched Product IDs:",
    completed_orders["Product Name"].isna().sum()
)

print(
    "Missing Unit Costs:",
    completed_orders["Unit Cost"].isna().sum()
)


# ------------------------------------------------------------
# 14. Save Processed Dataset
# ------------------------------------------------------------

completed_orders.to_csv(
    "Module-02-Data-Processing\\Pandas\\Capstone\\data\\completed_orders.csv",
    index=False
)

completed_orders.to_parquet(
    "Module-02-Data-Processing\\Pandas\\Capstone\\data\\completed_orders.parquet",
    index=False
)


# ------------------------------------------------------------
# 15. Final Inspection
# ------------------------------------------------------------

print("\nFinal dataset shape:")
print(completed_orders.shape)

print("\nFinal dataset:")
print(completed_orders.head())

print("\nMilestone 1 completed successfully.")