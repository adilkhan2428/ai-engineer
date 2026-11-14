class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = [] # list of (name, price)

    def add_item(self, name, price):
        self.items.append((name, price)) # This line takes the product name and price, package them into a tuple ('Rice 5kg', 850), and append to the self.items list.
        return f'Added: {name}' # give back a confirmation message.

    def total(self):
        return sum(p for _, p in self.items) # underscore _ is a convenstion meaning "we are ignoring the first element (the item name). p captures the second element (the price)"
    def receipt(self):
        lines = [f'Cart for {self.owner}:'] # start a list of strings to build the receipt line-by-line, beginning with the cart owner's name
    
        for name, price in self.items: # unpacke every item tuple in the cart
            lines.append(f'    {name}: PKR {price:,}') # price have added the comma separators for thousands, like 1,050
        
        lines.append(f'    TOTAL: PKR {self.total():,}') # Dynamically calls the total() method to get the final sum and append it.
        return '\n'.join(lines) # merges all the separate lines into a singl multi-lines string separated by newline characters (\n)
    



cart = ShoppingCart('Ali')

cart.add_item('Rice 5kg', 750)

cart.add_item('Milk 1L', 380)

print(cart.receipt())


    