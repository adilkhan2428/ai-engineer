# Closure: Function under the function, that remember outer value.

def discount_factory(percent):
    # outer value percent, that will be remembered.
    def apply_discount(price):
        return price * percent
    return apply_discount

ten_percent = discount_factory(0.9)
twenty_pecent = discount_factory(0.8)

print(ten_percent(1800))
print(twenty_pecent(1800))




