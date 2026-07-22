import pandas as pd
# Build from Scratch
# A Shopify merchant wants a report of fast deliveries with satisfied customers.
# Here in below line we filter the data.
df = pd.read_csv('Module-02-Data-Processing\\Pandas\\datasets\\ecommerce_sales_analytics_5000.csv')
report = df[(df['delivery_days'] <= 3) & (df['customer_rating'] >= 4)][ 
    [
        'order_id',
        'product_category',
        'region',
        'delivery_days',
        'customer_rating',
        'revenue'
    ]
]
print(report.head(15)) # Inspect the data
print(report.shape) 
report.info()  
print(report.describe()) # Understand the data
print(report['product_category'].value_counts())  # Select the data.
print(report['region'].value_counts())
