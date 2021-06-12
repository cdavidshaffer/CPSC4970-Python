from numbers import Number   # ABC for numbers
from collections.abc import MutableSequence


class BankAccount:
    """Your class docstring goes here!"""

    def __init__(self, account_number: int, owner: str) -> None:
        self.account_number = account_number
        self.owner = owner
        self._balance = 0

    def deposit(self, amount: Number) -> None:
        self._balance += amount

    def withdraw(self, amount: Number) -> None:
        self._balance -= amount

    def get_balance(self) -> Number:
        return self._balance

    def _set_balance(self, bal: Number) -> None:
        self._balance = bal

    def __str__(self) -> str:
        return f"Account number {self.account_number} "\
               f"owned by {self.owner} "\
               f"with balance {self._balance}"

    def __repr__(self) -> str:
        return f'BankAccount({self.account_number}, "{self.owner}") with balance {self._balance}'


class CheckingAccount(BankAccount):
    pass


if __name__ == "__main__":
    ba1: BankAccount = BankAccount(100, "Wilma")
    print(repr(ba1))
    accounts = [CheckingAccount(100, 'bob')]  # type: MutableSequence[BankAccount]

