import pandas as pd

df = pd.DataFrame({
    "customer_name": ["  AHMED", "sara  ", "BILAL"],
    "sale_date": ["2024-01-15", "bad_entry", "2024-03-10"],  
    "amount": [500, 300, 800]
})
# parse --> sort --> extract
# string data handling
df["customer_name"] = df["customer_name"].str.lower().str.strip()
# converting datetime into datetime object. (Parse)
df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")
# sorting order_date column (Sort)
df = df.sort_values("sale_date")
# extracting the components from order_date column (Extract)
df["month"] = df["sale_date"].dt.month

df["day_of_week"] = df["sale_date"].dt.day_of_week
print(df)
print(df.shape)