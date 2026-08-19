# 2. Function with a default argument

def apply_discount(price, percent=10):
    discount = price * percent / 100
    return price - discount


# Using only the price
print(apply_discount(1000))

# Using both arguments, with percent as a keyword argument
print(apply_discount(1000, percent=20))