class Wallet:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount


wallet = Wallet(1000)

wallet.deposit(500)
wallet.withdraw(200)

print(wallet.balance)