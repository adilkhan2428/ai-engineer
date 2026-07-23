import pandas as pd 

cost_df = pd.read_csv('Module-02-Data-Processing\\Pandas\\datasets\\product_cost_data.csv')
revenue_df = pd.read_csv('Module-02-Data-Processing\\Pandas\\datasets\\revenue_data.csv')
print('Revenue Dataset')
print(revenue_df.head())
print()
print('\nCost Dataset')
print(cost_df.head())
print('\nRevenue Dataset Shape')
print(revenue_df.shape)
print('\nCost Dataset shape')
print(cost_df.shape)
# merging both DataFrame using Category ID column 
merged_df = pd.merge(
    cost_df[['Category ID', "Cost"]],
    revenue_df,
    on="Category ID"
)
# printing marged DataFrame
print('\nMerged Dataset')
print(merged_df.head())
print('\nMerged Dataset Shape')
print(merged_df.shape)
# Level -- Exercise 2 (Business Analysis)
print('\nProduct Name')
print(merged_df[['Product Name', 'Revenue']])
print('\nRevenue')
print(merged_df["Revenue"])
print('\nCost')
print(merged_df["Cost"])
# another DataFrame containing (Product Name, Revenue, Cost)
revenu_cost_df = merged_df[['Product Name', 'Revenue', 'Cost']]
print('\nProfit DataFrame')
print(revenu_cost_df)

# -- Exercise 3 (Filtering)
electronics_df = merged_df[merged_df['Category'] == "Electronics"]
print('\nElectronics Dataset')
print(electronics_df.head())
print('\nElectronics Dataset shape')
print(electronics_df.shape)

# -- Exercise 4 (ExcelWriter) 
with pd.ExcelWriter("files_save_test\\Business_Report.xlsx") as writer: 
    revenue_df.to_excel(
        writer, 
        sheet_name="Revenue",
        index=False
    )
    cost_df.to_excel(
        writer, 
        sheet_name="Cost",
        index=False
    )
    merged_df.to_excel(
        writer, 
        sheet_name="Merged",
        index=False
    )
    electronics_df.to_excel(
        writer, 
        sheet_name="Electronics",
        index=False
    )

# Level 3 -- Production Scenario
high_revenue_products = revenue_df[revenue_df["Revenue"] > 30000]
with pd.ExcelWriter("files_save_test\\Daily_Shopify_Report.xlsx") as writer: 
    revenue_df.to_excel(
        writer, 
                sheet_name="Revenue",
                index=False
            )
    cost_df.to_excel(
        writer, 
            sheet_name="Cost",
            index=False
    )
    merged_df.to_excel(
        writer, 
            sheet_name="Merged",
            index=False
    )
    high_revenue_products.to_excel(
        writer, 
        sheet_name="High Revenue Products",
        index=False
    )

    