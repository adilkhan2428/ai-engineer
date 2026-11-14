# # ATM System
# user_input = input("How much money do you want to withdraw? ")

# try:
#     # We try to convert the text input into a whole number
#     amount = int(user_input)
#     print(f"Dispensing Rs. {amount}...")

# except ValueError:
#     # This triggers if they typed letters instead of numbers
#     print("Error: Please enter a valid number using numbers (e.g., 500), not words.")

# total_bill = 1200
# friends = int(input("How many friends are splitting the bill? "))

# try:
#     share = total_bill / friends
#     print(f"Each person pays: Rs. {share}")

# except ZeroDivisionError:
#     print("Error: You cannot split a bill among 0 people!")

# # We want this celebration message to show ONLY if everything went perfectly 
# else:
#     print("Thank you for dining with us! Transaction successful.")

# # We want this cleanup message to show NO MATTER WHAT happens
# finally:
#     print("System: Clearing temporary session data... Session closed.")


# # Challange 3: The Profile Bio Viewer (IndexError):
# hobbies = ["Coding", "Gaming", "Reading"]

# # 1. Ask the user for a number position
# choice = int(input("Enter hobby number (0, 1, or 2): "))

# try:
#     print(f"This is your hobby: {hobbies[choice]}")

# except IndexError:
#     print("That hobby position doesn't exist!")

# Exercise:  Handling Multiple "What - Ifs"
# try:
#     weight_input = input("Please enter your weight in KG: ")
#     weight = float(weight_input)

#     if weight <= 0:
#         raise ValueError("Weight Must be a positive number.")
#     print(f"Success! Your weight is updated to {weight} kg.")
# except ValueError:
#     print("Please enter the Number not text!")

connection_speed = int(input("Enter connection speed (Mbps): "))
file_size = 500  # 500 MB

try:
    # Calculate download time
    time_taken = file_size / connection_speed
    print(f"Downloading... Estimated time: {time_taken} seconds.")

# 1. CATCH THE ERROR IF SPEED IS 0
except ZeroDivisionError:
    print("Error: Connection speed cannot be zero!")

# 2. CELEBRATE IF DOWNLOAD SUCCEEDED
else:
    print("Download complete! File saved safely.")

# 3. DISCONNECT FROM SERVER NO MATTER WHAT
finally:
    print("System: Disconnecting from server... Connection closed safely.")









