class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"