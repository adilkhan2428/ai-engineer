import pandas as pd
jan_data = pd.DataFrame({
    "order_id": [1010],
    "customer_id": ["C01"],
    "product_id": ["P1"],
    "total": [59.99],
    "status": ["paid"]
})
feb_data = pd.DataFrame({
    "order_id": [1011],
    "customer_id": ["C02"],
    "product_id": ["P2"],
    "total": [45.99],
    "status": ["paid"]
})

print(pd.concat([jan_data, feb_data], axis=0))