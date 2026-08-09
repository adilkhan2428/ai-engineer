# Exercise: E-commerce Sales Intelligence 
# We have the raw order data from an online store. The data contains some messy values and the manager wants a clean sales analysis. 


# this is the realistic exercise for practicing the concepts of pandas like: Sorting and Ranking, rolling and expanding, groupby + rolling, dtype Optimization, changing to Numpy and storing the DataFrame. and ML handoff.
import pandas as pd

orders = pd.DataFrame({
    "Order ID": [1001, 1002, 1003, 1004, 1005, 1006,
                 1007, 1008, 1009, 1010, 1011, 1012],

    "Customer": ["Ali", "Sara", "Ali", "John", "Sara", "Ali",
                 "John", "Sara", "John", "Ali", "Sara", "John"],

    "Region": ["North", "South", "North", "West", "South", "North",
               "West", "South", "West", "North", "South", "West"],

    "Revenue": ["12000", "18000", "15000", "22000", "INVALID", "25000",
                "19000", "21000", "17000", "30000", "16000", "N/A"],

    "Cost": [7000, 11000, 9000, 14000, 10000, 15000,
             12000, 13000, 10000, 18000, 9500, 11000],

    "Units Sold": ["5", "8", "6", "10", "7", "12",
                   "9", "10", "six", "15", "7", "11"],

    "Customer Rating": [4.5, 4.2, 4.8, 4.1, 4.7, 4.9,
                        3.9, 4.6, 4.3, 4.9, 4.4, 4.0],

    "Date": pd.to_datetime([
        "2026-08-01", "2026-08-01", "2026-08-02", "2026-08-02",
        "2026-08-03", "2026-08-03", "2026-08-04", "2026-08-04",
        "2026-08-05", "2026-08-05", "2026-08-06", "2026-08-06"
    ])
})

# Part 1 -- Data Cleaning 
orders["Revenue"] = pd.to_numeric(
    orders["Revenue"],
    errors = "coerce"
)
orders["Units Sold"] = pd.to_numeric(
    orders["Units Sold"],
    errors = "coerce"
)
print("Dtypes after conversion")
print(orders.dtypes)
print("\nIdentify where missing values were created: ")
print(orders)

# Part 2 -- Feature Engineering 
orders["Profit"] = orders["Revenue"] - orders["Cost"]
orders["Revenue_Per_Unit"] = orders["Revenue"] / orders["Units Sold"]
print("\nOrders After new Features: ")
print(orders)

# Part 3 -- Customer Behavior 
# For each customer, calculate their:   2-order rolling average revenue
orders["Rolling_2_Day_Avg"] = orders.groupby("Customer")["Revenue"].transform(
    lambda x: x.rolling(window=2).mean()
)
print("\nOrder after rolling 2-Order average revenue: ")
print(orders)

# Part 4 -- Daily Sales Intelligence 
# create a daily sales DataFrame contaning total revenue fro each date.
daily_sales = orders.groupby("Date", as_index=False)["Revenue"].sum()
print("\nDaily Sales DataFrame")
print(daily_sales)
# now calculate: 3_Day_Rolling_Revenue, Cumulative_Revenue
daily_sales["3_Day_Rolling_Revenue"] = (
    daily_sales["Revenue"].rolling(3).sum()
)

daily_sales["Cumulative_Revenue"] = (
    daily_sales["Revenue"].expanding().sum()
)
print("\nDaily Sales after Rolling and expanding: ")
print(daily_sales)

# Part 5 -- Ranking 
orders["Revenue_Rank"] = orders["Revenue"].rank(
    ascending=False
)
print("\nOrders After Revenue Rank: ")
print(orders)

# Part 6 -- Region Analysis 
print("==========================")
regional_dashboard = orders.groupby("Region").agg(
    Total_Revenue = ("Revenue", "sum"),
    Average_Revenue = ("Revenue", "mean"),
    Total_Units_Sold = ("Units Sold", "sum"),
    Total_Orders = ("Order ID", "count"),
    Average_Customer_Rating = ("Customer Rating", "mean")
)
print("\nRegional Dashboard: ")
print(regional_dashboard)
print("=========================")

# Part 7 -- Memory Optimization 
print("\nInspect Memory Usage of Order DataFrame: ")
print(orders.memory_usage(deep=True)) # Region and Customer are good condidates for category
print()
# Convert Region and Customer to category dtype
orders[["Region", "Customer"]] = orders[["Region", "Customer"]].astype("category")
print("\nAfter convert orders Memory Usage: ")
print(orders.memory_usage(deep=True))

# Part 8 -- ML Handoff 
orders["Repeat Customer"] = orders.groupby("Customer", observed = True)["Order ID"].transform("count") > 1

X = orders[
    [
    "Revenue",
    "Cost",
    "Units Sold",
    "Customer Rating"
]
    ].to_numpy()
y = orders["Repeat Customer"].to_numpy()

orders.to_parquet("PATH/clean_orders.parquet")
loaded_orders = pd.read_parquet("PATH/clean_orders.parquet")

print(loaded_orders.shape)
print(loaded_orders.dtypes)