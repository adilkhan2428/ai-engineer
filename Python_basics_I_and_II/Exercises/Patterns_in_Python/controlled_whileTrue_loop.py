store_inventory = {"pen": 50, "notebook": 120, "eraser": 200}

while True:
    # Always convert user input to lowercase right away
    user = input("Enter a product name (or 'quit' to stop): ").lower()
    
    # 1. Check for exit first
    if user == "quit" or user == "done":
        print("Goodbye!")
        break
        
    # 2. Check if it exists in the dictionary
    elif user in store_inventory:
        print(f"{user} stock: {store_inventory[user]}")
        
    # 3. Handle errors gracefully
    else:
        print("Item not found in inventory.")