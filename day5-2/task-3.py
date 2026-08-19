class Account:
    def get_interest_rate(self):
        return 4


class SavingsAccount(Account):
    def get_interest_rate(self):
        return 5


class FixedDeposit(Account):
    def get_interest_rate(self):
        return 7


accounts = [
    Account(),
    SavingsAccount(),
    FixedDeposit()
]

for account in accounts:
    print("Interest rate:", account.get_interest_rate(), "%")