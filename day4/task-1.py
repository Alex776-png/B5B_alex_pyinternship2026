def build_invoice(customer_name, *args, **kwargs):
    total = sum(args)

    print("Customer:", customer_name)
    print("Total:", total)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


build_invoice(
    "Musashi Tsukiyama",
    100, 250, 150,
    discount=20,
    tax=50
)