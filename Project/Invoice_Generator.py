from datetime import datetime


def get_number(prompt, number_type=float):
    while True:
        try:
            value = number_type(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_line():
    print("-" * 70)


def generate_invoice():
    print("\n")
    print("=" * 70)
    print("                    INVOICE GENERATOR")
    print("=" * 70)

    # --------------------------------------------------
    # Business details
    # --------------------------------------------------

    print("\nBUSINESS DETAILS")
    print_line()

    business_name = input("Business Name: ")
    business_phone = input("Business Phone: ")
    business_address = input("Business Address: ")
    gstin = input("GSTIN (optional): ")

    # --------------------------------------------------
    # Customer details
    # --------------------------------------------------

    print("\nCUSTOMER DETAILS")
    print_line()

    customer_name = input("Customer Name: ")
    customer_phone = input("Customer Phone: ")
    customer_address = input("Customer Address: ")

    # --------------------------------------------------
    # Invoice details
    # --------------------------------------------------

    invoice_number = input("Invoice Number: ")

    if not invoice_number:
        invoice_number = "INV-" + datetime.now().strftime("%Y%m%d%H%M%S")

    invoice_date = input("Invoice Date (DD-MM-YYYY): ")

    if not invoice_date:
        invoice_date = datetime.now().strftime("%d-%m-%Y")

    # --------------------------------------------------
    # Products
    # --------------------------------------------------

    print("\nPRODUCT / SERVICE DETAILS")
    print_line()

    items = []

    number_of_items = int(
        get_number(
            "How many products/services? ",
            int
        )
    )

    for i in range(number_of_items):
        print(f"\nItem {i + 1}")

        description = input("Product/Service Name: ")

        quantity = get_number("Quantity: ")
        price = get_number("Price per unit: ")

        amount = quantity * price

        items.append({
            "description": description,
            "quantity": quantity,
            "price": price,
            "amount": amount
        })

    # --------------------------------------------------
    # Calculations
    # --------------------------------------------------

    subtotal = sum(item["amount"] for item in items)

    print("\nTAX & DISCOUNT")
    print_line()

    discount_percent = get_number(
        "Discount (%): "
    )

    gst_percent = get_number(
        "GST (%): "
    )

    discount_amount = subtotal * discount_percent / 100

    taxable_amount = subtotal - discount_amount

    gst_amount = taxable_amount * gst_percent / 100

    grand_total = taxable_amount + gst_amount

    # --------------------------------------------------
    # PRINT INVOICE
    # --------------------------------------------------

    print("\n\n")
    print("=" * 70)
    print("                         INVOICE")
    print("=" * 70)

    print(f"Invoice No : {invoice_number}")
    print(f"Date       : {invoice_date}")

    print_line()

    print("BUSINESS")
    print(f"Name       : {business_name}")
    print(f"Phone      : {business_phone}")
    print(f"Address    : {business_address}")

    if gstin:
        print(f"GSTIN      : {gstin}")

    print_line()

    print("BILL TO")
    print(f"Name       : {customer_name}")
    print(f"Phone      : {customer_phone}")
    print(f"Address    : {customer_address}")

    print_line()

    # --------------------------------------------------
    # Product table
    # --------------------------------------------------

    print(
        f"{'No.':<5}"
        f"{'Product/Service':<30}"
        f"{'Qty':>8}"
        f"{'Price':>12}"
        f"{'Amount':>12}"
    )

    print_line()

    for i, item in enumerate(items, start=1):
        print(
            f"{i:<5}"
            f"{item['description'][:29]:<30}"
            f"{item['quantity']:>8.2f}"
            f"{item['price']:>12.2f}"
            f"{item['amount']:>12.2f}"
        )

    print_line()

    # --------------------------------------------------
    # Totals
    # --------------------------------------------------

    print(f"{'Subtotal':>55} : ₹{subtotal:,.2f}")
    print(
        f"{'Discount':>55} : "
        f"₹{discount_amount:,.2f}"
    )
    print(
        f"{'Taxable Amount':>55} : "
        f"₹{taxable_amount:,.2f}"
    )
    print(
        f"{'GST (' + str(gst_percent) + '%)':>55} : "
        f"₹{gst_amount:,.2f}"
    )

    print_line()

    print(
        f"{'GRAND TOTAL':>55} : "
        f"₹{grand_total:,.2f}"
    )

    print("=" * 70)
    print("                 THANK YOU FOR YOUR BUSINESS!")
    print("=" * 70)

    print("\n")


# ------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------

while True:

    generate_invoice()

    again = input(
        "Do you want to create another invoice? (y/n): "
    ).lower()

    if again != "y":
        print("\nThank you. Goodbye!")
        break
