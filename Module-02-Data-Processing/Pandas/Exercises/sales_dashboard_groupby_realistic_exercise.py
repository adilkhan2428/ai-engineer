import pandas as pd

df = pd.DataFrame({
    "Order ID": [
        1001,1002,1003,1004,1005,1006,
        1007,1008,1009,1010,1011,1012,
        1013,1014,1015
    ],

    "Customer":[
        "Ali","Sara","Ali","John","Fatima",
        "Sara","Ahmed","Ali","John","Fatima",
        "Ahmed","Sara","Ali","John","Fatima"
    ],

    "Region":[
        "North","South","North","East","West",
        "South","North","West","East","North",
        "West","South","North","East","West"
    ],

    "Category":[
        "Electronics","Furniture","Electronics",
        "Accessories","Furniture",
        "Electronics","Accessories",
        "Furniture","Electronics",
        "Accessories","Furniture",
        "Accessories","Electronics",
        "Furniture","Accessories"
    ],

    "Product":[
        "Laptop","Desk","Phone",
        "Mouse","Chair",
        "Keyboard","USB Cable",
        "Table","Monitor",
        "Power Bank","Sofa",
        "Mouse Pad","Tablet",
        "Wardrobe","Charger"
    ],

    "Units Sold":[
        2,1,3,5,2,
        4,8,1,2,6,
        1,7,2,1,9
    ],

    "Revenue":[
        240000,18000,150000,
        7500,30000,
        40000,8000,
        22000,60000,
        18000,55000,
        14000,90000,
        70000,27000
    ],

    "Customer Rating":[
        4.8,4.2,4.9,
        4.4,4.1,
        4.7,4.5,
        4.0,4.8,
        4.6,4.3,
        4.4,4.9,
        4.2,4.7
    ],

    "Salesperson":[
        "Ayesha","Bilal","Ayesha",
        "Hamza","Bilal",
        "Ayesha","Hamza",
        "Bilal","Ayesha",
        "Hamza","Bilal",
        "Hamza","Ayesha",
        "Bilal","Hamza"
    ]
})


# Executive Sales Dashboard 
# 1. Region Dashboard using named aggregation

region_dashboard = df.groupby("Region").agg(
    Total_Revenue = ('Revenue', 'sum'),
    Average_Revenue = ("Revenue", 'mean'),
    Total_Units_Sold = ('Units Sold', 'sum'),
    Total_Orders = ('Order ID', 'count'),
    Average_Customer_Rating = ('Customer Rating', 'mean')
).sort_values("Total_Revenue", ascending=False)
print(region_dashboard)
# 2. Add a new column to the original DataFrame: Region_Avg_Revenue
df["Region_Avg_Revenue"] = df.groupby("Region")["Revenue"].transform('mean')
# 3. Add another column: Revenue_vs_Region_Avg
df["Revenue_vs_Region_Avg"] = df["Revenue"] - df["Region_Avg_Revenue"]
print(df)
print()
# 4. Create a DataFrame containing only regions whose: Total Revenue is greater than 150,000
high_value_region = df.groupby("Region").filter(
    lambda x: x["Revenue"].sum() > 150000
)
print(high_value_region)