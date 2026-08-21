products = {
    "Laptop": 10000,
    "Mouse": 120,
    "Keyboard": 800,
    "Monitor": 12000,
    "Headphones": 670,
    "USB Cable": 20
}

expensive_products = {
    product: price
    for product, price in products.items()
    if price > 100
}

print(expensive_products)