import pandas as pd

customers_df = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105],
    "customer_name": ["Adil", "Abbas", "Hamza", "Ali", "Ahmed"],
    "city": ["Peshawar", "Lahore", "Islamabad", "Karachi", "Quetta"],
    "membership": ["Gold", "Silver", "Gold", "Bronze", "Silver"]
})

orders_df = pd.DataFrame({
    "order_id": [5001, 5002, 5003, 5004],
    "customer_id": [101, 102, 104, 106],
    "city": ["Islamabad", "Lahore", "Karachi", "Multan"],
    "revenue": [12000, 8500, 9500, 15000]
})

print(customers_df)
print()
print(orders_df)
print()
customer_report = pd.merge(customers_df, orders_df, on= "customer_id", how= 'left', suffixes= ("_customer", "_order"))
print(customer_report)