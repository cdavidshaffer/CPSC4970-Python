from copy import deepcopy


class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def print(self):
        print(f"Transaction: {self.description}: {self.amount}")


class BankAccount:
    """Your class docstring goes here!"""

    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self._balance = 0
        self._transactions = []

    def deposit(self, amount):
        self._transactions.append(Transaction("deposit", amount))
        self._balance += amount

    def withdraw(self, amount):
        self._transactions.append(Transaction("withdraw", -amount))
        self._balance -= amount

    def get_transactions(self):
        return deepcopy(self._transactions)

    def add_transaction(self, d, a):
        self._transactions.append(Transaction(d, a))
        self._balance += a

    def get_balance(self):
        return self._balance

    def print(self):
        print(f"Account number {self.account_number} "
              f"owned by {self._owner} "
              f"with balance {self._balance}")


class CheckingAccount(BankAccount):
    pass


class SavingsAccount(BankAccount):
    def accrue_interest(self):
        self._balance += 0.001 * self._balance


if __name__ == "__main__":
    ba1 = CheckingAccount(100, "Wilma")
    ba1.owner = "Foo"
    print(ba1.owner)
