
sales = {'hoodie': 1800, 'shirt': 1200, 'cap': 600}
# add 200 profit to each
new_sales = {item: price + 200 for item, price in sales.items()}
# this will add 200 profit to each 
# {'hoodie': 2000, 'shirt': 1400, 'cap': 800}
print(new_sales)