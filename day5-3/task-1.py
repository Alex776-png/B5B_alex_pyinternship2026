import time


# 1. Wallet
class Wallet:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount