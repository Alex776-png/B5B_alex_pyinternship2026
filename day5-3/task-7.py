class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        elapsed = end_time - self.start_time
        print(f"Time elapsed: {elapsed:.6f} seconds")


# -------------------------
# Testing
# -------------------------

# 1. Wallet
wallet = Wallet(100)
wallet.deposit(50)
wallet.withdraw(30)
print("Wallet balance:", wallet.balance)


# 2. Fraction
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
result = f1 + f2
print("Fraction:", result)  # 5/6


# 3. Inventory
inventory = Inventory()
inventory.add_item("Laptop")
inventory.add_item("Mouse")
inventory.add_item("Keyboard")

print("Inventory length:", len(inventory))
print("First item:", inventory[0])


# 4. Point
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(5, 6)

print("Point:", p1)
print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)


# 5. Stack
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

print("Stack:", stack)
print("Popped:", stack.pop())
print("Stack after pop:", stack)


# 6. Money
money1 = Money(100, "USD")
money2 = Money(150, "USD")

print("money1 < money2:", money1 < money2)
print("money1 > money2:", money1 > money2)

# This raises ValueError:
# money1 < Money(50, "EUR")


# 7. Timer
with Timer():
    for i in range(1_000_000):
        pass