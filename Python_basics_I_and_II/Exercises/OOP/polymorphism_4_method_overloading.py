# Method ovelaoding: is the idea of having same method name, to handle different input compositions.
# Exercise no: 1
# class Order:
#     def calculate_total(self, *prices):
#         return sum(prices)

# order = Order()

# print(order.calculate_total(10, 20, 30, 40, 50, 60))
# print(order.calculate_total())

# Exercise no: 2
class Order: 
    def calculate_total(self, *prices,  shipping= 0):
        return sum(prices) + shipping

order = Order()
print(order.calculate_total(100, 200, 300))
print(order.calculate_total(100, 200, shipping=150))
print(order.calculate_total())