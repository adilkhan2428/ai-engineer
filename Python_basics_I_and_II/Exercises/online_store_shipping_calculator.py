# Imagine you are building a checkout system. You need a function that calculates if an order qualifies for free delivery.

# Here is the function already built for you:

def calculate_shipping(order_amount):
    if order_amount >= 2000:
        return 0  # Free shipping!
    else:
        return 200  # Rs. 200 delivery fee

# Your Mission:
# Write the code that comes after this function. You need to:

# Create a variable called cart_total = 1500 (representing a customer's shopping cart).

# Call the calculate_shipping function, pass your cart_total into it, and catch the returned value in a new variable called shipping_fee.

# Print out the final total amount (cart total + shipping fee).

# cart_total = 1800
# shipping_fee = calculate_shipping(cart_total)

# final_total = cart_total + shipping_fee
# print(f"Final Total: {final_total}")


fleet_vehicles = {
    "Civic": 42,
    "F-150": 18,
    "Prius": 55,
    "Transit Van": 14,
    "Corolla": 35
}

def get_efficiency_rating(mpg):
    if mpg >= 45:
        return "High Efficiency"
    elif mpg >= 30:
        return "Moderate Efficiency"
    elif mpg >= 15:
        return "Low Efficiency"
    else:
        "Gas Guzzler"


for vehicle, mpg in fleet_vehicles.items():
    print(f"{vehicle}: {mpg}")

