import pandas as pd

df = pd.read_csv("PATH")
# Task 1: Inspect the data
print(df.head())
#print(df.isna().sum())
# Task 2: Customer rating
df["Customer Rating"] = df["Customer Rating"].fillna(
    df["Customer Rating"].median()
)
# Task 3: Profit
df["Profit"] = df["Profit"].fillna(df["Profit"].mean())
# Task 4: Revenue
df["Revenue"] = df['Revenue'].interpolate()
# Task 5: Units sold
df["Units Sold"] = df["Units Sold"].interpolate()
# Task 6: Discount 
df["Discount"] = df["Discount"].ffill()
# Task 7: Remaining Missing Discounts 
df["Discount"] = df["Discount"].bfill()
# Final Quality Check 
print(df.isnull().sum())
print("\nTotal missing values in the dataset")
print(df.isnull().sum().sum())
# Task 9: Remove invalid Records 
# there is no any missing values any more so df.dropna() don't need here. 
# Task 10: Save the cleaned dataset
df.to_excel("clean_ecommerce_sales.xlsx", index=False)