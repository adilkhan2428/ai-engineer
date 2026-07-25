import pandas as pd
def year_converter(value):
    if isinstance(value, str):
        value = value.replace("FY", "")
    return int(value)
def units_converter(value):
    if isinstance(value, str):
        value = value.replace("units", "").strip()
    return int(value)

def revenue_converter(revenue):
    if isinstance(revenue, str):
        revenue = revenue.replace("$", "").replace(",", "").strip()
    return float(revenue)
EXCELLENT_THRESHOLD = 7000
GOOD_THRESHOLD = 4000

def performance(value):
    if pd.isna(value):
        return "Unknown"
    elif value >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif value >= GOOD_THRESHOLD:
        return "Good"
    else:
        return "Average"
clean_df = pd.read_excel("Module-02-Data-Processing\\Pandas\\datasets\\ecommerce_data_file_handling_practice.xlsx",header=2,nrows=15, names= ["year", "category", "region", "units", "revenue"], na_values= ["Not Available", "N.A",
"n.a"],
converters= {
    "year": year_converter,
    "units": units_converter,
    "revenue": revenue_converter
}
)
clean_df.replace(-1, pd.NA, inplace=True)
clean_df['Tax'] = clean_df['revenue'] * 0.18
clean_df["Net Revenue"] = clean_df["revenue"] - clean_df["Tax"]
clean_df["Performance"] = clean_df["revenue"].apply(performance)
print(clean_df)
clean_df.to_excel("files_save_test\\clean_sales_report.xlsx", index=False)