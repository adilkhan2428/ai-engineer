# Operator Overloading: means defining what symbol like: (+ - * / etc) 
# mean for your own objects by writing special dunder methods. double underscore both e.g: __add__

# Exercise: Addition
# class Invoice:
#     def __init__(self, amount):
#         self.amount = amount

#     # Complete this method
#     def __add__(self, other):
#         return self.amount + other.amount


# invoice_a = Invoice(8000)
# invoice_b = Invoice(3000)
# print(invoice_a + invoice_b)  # Expected: 11000
# # when python encounter this it internallyze invokes: invoice_a.__add__(invoice_b)

# Exercise: Subtraction
# class Invoice:
#     def __init__(self, amount):
#         self.amount = amount
#     def __sub__(self, other):
#         return self.amount - other.amount
# invoice_a = Invoice(12000)
# invoice_b = Invoice(4000)

# total = invoice_a - invoice_b

# print(total)

# Exercise; Multiplication:
class Product:
    def __init__(self, amount):
        self.amount = amount
    def __mul__(self, other):
        return self.amount * other

product = Product(800)
quantity = 4
total = product * quantity
print(total)
