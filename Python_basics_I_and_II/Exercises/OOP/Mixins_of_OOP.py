# # Mixin pattern — common in AI frameworks like LangChain
# class LoggerMixin:
#     def log(self, message):
#         print(f'[LOG] {self.__class__.__name__}: {message}')

# class ValidatorMixin:
#     def validate(self, data):
#         if not data:
#             raise ValueError('Data cannot be empty!')
#         return True

# class SerializerMixin:
#     def to_dict(self):
#         return self.__dict__   # converts all attrs to dict

# # Main class inherits from all three mixins
# class User(LoggerMixin, ValidatorMixin, SerializerMixin):
#     def __init__(self, name, email, role):
#         self.name  = name
#         self.email = email
#         self.role  = role

#     def save(self):
#         self.validate(self.name)        # from ValidatorMixin
#         self.log(f'Saving user {self.name}')  # from LoggerMixin
#         return True

# u = User('Ali', 'ali@smit.edu', 'student')
# u.save()
# # [LOG] User: Saving user Ali
# print(u.to_dict())  # from SerializerMixin
# # {'name': 'Ali', 'email': 'ali@smit.edu', 'role': 'student'}
# print(User.__mro__)  # Method Resolution Order

# E-Commerce Product Management System with Mixins

# 1. Logger Mixin
class LoggerMixin:
    def log(self, action):
        # Added {action} so it actually prints what you pass into it!
        print(f"[PRODUCT LOG] {self.__class__.__name__}: {action}")

# 2. Discount Mixin
class DiscountMixin:
    def apply_discount(self, percentage):
        discount_amount = self.price * percentage
        self.price = self.price - discount_amount  # Subtract discount and update price
        return self.price

# 3. Serializer Mixin
class SerializerMixin:
    def to_dict(self):
        return self.__dict__   # Converts all attributes to a dictionary

# 4. Main Class using Multiple Inheritance (Mixins)
class ShopifyProduct(LoggerMixin, DiscountMixin, SerializerMixin):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        # Calling log from LoggerMixin
        self.log(f"Stock updated by {quantity} units. Current stock: {self.stock}")
        return True

# --- Testing the System ---
u = ShopifyProduct('Wireless Earbuds', 5000, 20)

# Test discount mixin
new_price = u.apply_discount(0.2)
print(f"New Price after 20% discount: PKR {new_price}")

# Test logger mixin via update_stock
u.update_stock(5)

# Test serializer mixin
print(u.to_dict())
print()

# Test Method Resolution Order (MRO)
print(ShopifyProduct.__mro__)