coupons = [("SAVE20", "Valid"), ("FRAUD100", "Blocked"), ("WELCOME", "Valid")]

for code, status in coupons:
    # The ':<12' forces the string to take exactly 12 spaces, left-aligned
    print(f"Coupon: {code:<12} | Status: {status}")
