class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def _check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies.")

    def __lt__(self, other):
        self._check_currency(other)
        return self.amount < other.amount

    def __gt__(self, other):
        self._check_currency(other)
        return self.amount > other.amount

    def __str__(self):
        return f"{self.amount} {self.currency}"