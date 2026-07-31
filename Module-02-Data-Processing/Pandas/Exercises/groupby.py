# Exercise: this exercise demonstrate how to use groupby() with multiple columns, the idea of: split --> apply --> combine
import pandas as pd

df = pd.read_excel("PATH")

regional_dashboard = df.groupby(["Region", "Category"], as_index=False).agg({
    "Revenue": 'sum', 
    "Customer Rating": 'mean',
    "Unit Sold": 'sum',
    "Salesperson": 'count'
})
print(regional_dashboard)