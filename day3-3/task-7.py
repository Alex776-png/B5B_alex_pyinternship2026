inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

def add_stock(product, quantity):
    inventory[product] = inventory.get(product, 0) + quantity
    print(quantity, product, "added to inventory.")


def sell_product(product, quantity):
    if product not in inventory:
        print("Error:", product, "does not exist in inventory.")
    elif inventory[product] < quantity:
        print("Error: Not enough stock for", product)
    else:
        inventory[product] -= quantity
        print(quantity, product, "sold successfully.")


# Add new stock
add_stock("Laptop", 5)

# Add a completely new product
add_stock("Headphones", 10)

# Sell existing product
sell_product("Mouse", 3)

# Try to sell a product that does not exist
sell_product("Tablet", 2)

# Try to sell more than available stock
sell_product("Keyboard", 20)

print("\nFinal Inventory:")
print(inventory)