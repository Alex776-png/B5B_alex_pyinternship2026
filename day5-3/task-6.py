class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies are different")

    def __lt__(self, other):
        self.check_currency(other)
        return self.amount < other.amount

    def __gt__(self, other):
        self.check_currency(other)
        return self.amount > other.amount


m1 = Money(500, "USD")
m2 = Money(700, "USD")

print(m1 < m2)
print(m1 > m2)