# This is pattern no. 1: The dictionary loop + function caller 
# in which we have the dictionary and loop through and have the function which we call. 

# Task P1. 
# we have a dictionary of laptop batteries and their current charge percentages

# batteries = {"HP": 45, "Dell": 15, "MacBook": 90}
# # 1. The Function (Does the math for a single item)
# def battery(percent):
#     if percent < 20:
#         return "Critical"
#     elif percent <= 50:
#         return "Low"
#     else:
#         return "Good"
# # 2. The Loop (Scans through every item in the dictionary)
# for name,percent in batteries.items():
#     status = battery(percent)
#     print(f"{name}: {status}")

# Task P2: Restaurant Item Status Check
prep_times = {  # restaurant menu and their preparation time in minutes.
    "Biryani": 25,
    "Burger": 10,
    "Family Platter": 50,
    "Fries": 5
}

def speed_status(minutes):
    if minutes <= 10:
        return "Express"
    elif minutes <= 30:
        return "Standard"
    else:
        return "Delayed"

for item, times in prep_times.items():
    status = speed_status(times)
    print(f"{item}: {status}")
