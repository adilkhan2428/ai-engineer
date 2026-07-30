import pandas as pd

# 1. Load the dataset (update path if running locally vs Google Colab)
# df = pd.read_csv("PATH")
df = pd.read_csv("shopify_orders_sample.csv")

print("=== 1. Index Manipulation (.set_index & .loc / .iloc) ===")
# Set 'order_id' as the custom row label index
df.set_index("order_id", inplace=True)

# Access a specific row by its label using .loc
print("Row for order_id 1003:")
print(df.loc[1003])
print()

# Access rows by integer position using .iloc (exclusive of upper bound 3)
print("First 3 rows using .iloc:")
print(df.iloc[:3])
print()

# Restore standard numeric range index
df.reset_index(inplace=True)


print("=== 2. Boolean Masking & Complex Filtering ===")
# Create and apply a boolean mask for totals greater than 150.0
mask = df['total'] > 150.0
print("Orders with total > 150.0:")
print(df.loc[mask])
print()

# Complex bitwise filtering: total > 180 AND status == 'Fulfilled' AND region != 'West'
complex_filter = (df['total'] > 180.0) & (df["status"] == 'Fulfilled') & ~(df["region"] == "West")
print("Filtered Orders (Total > 180, Fulfilled, Non-West):")
print(df.loc[complex_filter])
print()


print("=== 3. Membership Filtering (.isin) ===")
# Filter rows where region is either North or East
north_east_orders = df[df["region"].isin(["North", "East"])]
print("Orders in North or East regions:")
print(north_east_orders[['order_id', 'customer', 'region', 'total']])
print()

# Negated .isin: Exclude Cancelled and Pending statuses (keeps only active/fulfilled)
active_orders = df[~df["status"].isin(["Cancelled", "Pending"])]
print("Active Orders (Excluding Cancelled & Pending):")
print(active_orders[['order_id', 'customer', 'status', 'total']])
print()


print("=== 4. String-Based Filtering (.query) ===")
# Clean, human-readable string expression query equivalent to complex bitwise filter
query_result = df.query('total > 100.0 and status == "Fulfilled" and region != "West"')
print("Query Result (total > 100, Fulfilled, region != West):")
print(query_result[['order_id', 'customer', 'total', 'status', 'region']])