def process_order(order):
    try:
        item = order["item"]
        price = order["price"]

    except KeyError as e:
        print(f"Error: Missing required order key: {e}")

    else:
        print(f"Item: {item}")
        print(f"Price: {price}")
        print("Order details are valid.")

    finally:
        print("Processing complete")

process_order({"item": "Laptop", "price": 50000}) #valid

process_order({"item": "Laptop"}) #missing