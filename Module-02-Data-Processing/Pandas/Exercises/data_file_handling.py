from pathlib import Path

import pandas as pd


def year_converter(value):
    if isinstance(value, str):
        value = value.replace("FY", "")
        return int(value)
    return int(value)


def unit_sold_converter(units):
    if isinstance(units, str):
        units = units.replace("units", "")
        return int(units)
    return int(units)


def revenue_converter(revenue):
    if isinstance(revenue, str):
        revenue = revenue.replace("$", "").replace(",", "")
        return int(revenue)
    return int(revenue)

def performance(value):
    if value.isna().any().any():
        return "Unknown"
    elif value.revenue >= 7000:
        return "Excellent"
    elif value.revenue >= 4000:
        return "Good"
    else: 
        return "Average"





df = pd.read_excel('Module-02-Data-Processing\\Pandas\\datasets\\ecommerce_data_file_handling_practice.xlsx',
    header=2,
    names=["year", "category", "region", "units", "revenue"],
    nrows=8,
    na_values=["N.A", "n.a", "Not Available"],
    converters={
        "year": year_converter,
        "units": unit_sold_converter,
        "revenue": revenue_converter,
    },
)
df = df.replace(-1, pd.NA)

print(df.head())
print(df.isna().sum())  # category column has the most missing values.

df["Tax"] = df["revenue"] * 0.18
df["Net Revenue"] = df["revenue"] - df["Tax"]
df["Performance"] = df.performance

