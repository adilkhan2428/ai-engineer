security_clearance = {"Ali": "Admin", "Sara": "Manager", "Ahmed": "Staff"}
user_to_click = "Usman"

if user_to_click in security_clearance:
    print(f"{user_to_click} clearance: {security_clearance[user_to_click]}")
else:
    print('Access Denied: User not found.')