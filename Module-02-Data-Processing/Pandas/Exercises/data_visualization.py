import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("Module-02-Data-Processing\\Pandas\\datasets\\annual_sale_data.csv")
plt.plot(df["Year"],df["Phones"], color= "Orange", label= "Phones")
plt.plot(df["Year"], df["Laptops"], color= "Brown", label= "Laptops")
plt.plot(df["Year"], df["Monitors"], color= "Green", label="Monitors")
plt.title("Product Annual Sale")
plt.ylabel("Prouducts Revenue")
plt.xlabel("Sale Years")
plt.legend()
print(df)
plt.show()