products = {
    "Laptop": 750,
    "Mouse": 25,
    "Keyboard": 120,
    "Monitor": 300,
    "Headphones": 150,
    "USB Cable": 15
}

expensive_products = {
    product: price
    for product, price in products.items()
    if price > 100
}

print(expensive_products)