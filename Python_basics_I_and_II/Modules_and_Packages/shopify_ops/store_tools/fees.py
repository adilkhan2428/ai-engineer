def calculate_gateway_fee(order_total, rate=0.029, flat_fee=0.30):
    return round((order_total * rate) + flat_fee, 2)

# This block ONLY runs if you execute fees.py directly in VS Code
if __name__ == "__main__":
    print("Testing fee logic directly:", calculate_gateway_fee(100.00))
