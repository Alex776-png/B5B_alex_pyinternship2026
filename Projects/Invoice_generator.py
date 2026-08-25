#logic
def calculate_invoice(quantity, price, gst_rate):
    amount = quantity * price
    gst = amount * gst_rate / 100
    total = amount + gst

    return amount, gst, total

#display
def show_invoice(seller, customer, product, quantity, price, amount, gst, total):
    print("\n========== INVOICE ==========")
    print("Seller   :", seller)
    print("Customer :", customer)
    print("-----------------------------")
    print("Product  :", product)
    print("Quantity :", quantity)
    print("Price    : ₹", price)
    print("Amount   : ₹", amount)
    print("GST      : ₹", gst)
    print("-----------------------------")
    print("TOTAL    : ₹", total)
    print("=============================")


seller = input("Enter seller name: ")
customer = input("Enter customer name: ")

while True:

    print("\n===== MENU =====")
    print("1. Create Invoice")
    print("2. Exit")

    choice = input("Enter your choice: ")
    
    match choice:

        case "1":
            product = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            gst_rate = 18

            amount, gst, total = calculate_invoice(
                quantity, price, gst_rate
            )

            show_invoice(
                seller,
                customer,
                product,
                quantity,
                price,
                amount,
                gst,
                total
            )

        case "2":
            print("Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")