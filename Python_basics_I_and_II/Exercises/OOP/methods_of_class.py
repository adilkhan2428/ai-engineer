class Product:

    class Inventory:
        def __init__(self, stock_count, warehouse_location):
            self.stock_count = stock_count
            self.warehouse_location = warehouse_location

    def __init__(self, name, stock_count, warehouse_location):
        self.name = name

        self.inventory = Product.Inventory(stock_count, warehouse_location)

product_1 = Product("Mechanical keyboard", 45, "WH-North")
product_2 = Product("Wireless Mouse", 120, "WH-South")

print("---- product 1 ----")
print("Product name:", product_1.name)
print("Product stock:", product_1.inventory.stock_count)
print("Product warehouse:", product_1.inventory.warehouse_location)

print("---- product 2 ----")
print("Product name:", product_2.name)
print("Product stock:", product_2.inventory.stock_count)
print("Product warehouse:", product_2.inventory.warehouse_location)