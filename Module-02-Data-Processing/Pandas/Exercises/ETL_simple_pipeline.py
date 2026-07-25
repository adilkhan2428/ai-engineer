import pandas as pd
# Exercise 2 -- Build Three New Converters
def items_converter(value):
    if isinstance(value, str):
        value = value.replace("items", "").strip()
    return int(value)
def order_value_converter(value):
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "").strip()
    return float(value)
def shipping_converter(value):
    if isinstance(value, str):
        value = value.replace("FREE", "0").replace("$", "").strip()
    return float(value)
# Exercise 1 -- Data Loader (Easy)
# Exercise 3 -- Missing Values
df = pd.read_excel("Module-02-Data-Processing\\Pandas\\datasets\\lecture4_practice_marketplace.xlsx", header= 2, nrows= 8, names=["order_id", "order_date", "country", "platform", "items", "order_value", "shipping_fee", "coupon"], converters= {
    "items": items_converter,
    "order_value": order_value_converter,
    "shipping_fee": shipping_converter
}, na_values= ["N.A", "n.a", "Not Available"])
df = df.replace(-1, pd.NA, inplace=True)
print(df.isna().sum()) # coupen column have the most missing values.
print(df.isna().sum(axis=1)) # row: 2 have most missing values.
# Exercise 4 -- Business Columns
df["Tax"] = df["order_value"] * 0.08
df["Total_Cost"] = df["order_value"] + df["shipping_fee"]
df["Net Revenue"] = df["Total_Cost"] - df["Tax"]
# performance Function
VIP_THRESHOLD = 12000
EXCELLENT_THRESHOLD = 7000
GOOD_THRESHOLD = 3000
def performance(value):
    if pd.isna(value):
        return "Unknown"
    elif value >= VIP_THRESHOLD:
        return "VIP"
    elif value >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif value >= GOOD_THRESHOLD:
        return "Good"
    else:
        return "Average"    
df["Performance"] = df["order_value"].apply(performance)
# Exercise 6 -- Shipping status
df["Shipping Status"] = df["shipping_fee"].apply(
    lambda x: "Free Shipping" if x == 0 else "Paid Shipping"
)
# Exercise 7 -- Coupen Status
def coupen_status(value):
    if pd.isna(value):
        return "Unknown"
    elif value == "NONE":
        return "No Coupen"
    else: 
        return "Coupen Applied"
df["Coupen Status"] = df["coupen"].apply(coupen_status)
print(df)
df.to_excel("files_save_test\\marketplace_clean_report.xlsx", index=False)