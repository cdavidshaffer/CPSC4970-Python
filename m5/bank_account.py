class BankAccount:
    """Your class docstring goes here!"""

    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account number {self.account_number} "\
               f"owned by {self.owner} "\
               f"with balance {self._balance}"

    def __repr__(self):
        return f'BankAccount({self.account_number}, "{self.owner}") with balance {self._balance}'

    def write_to(self, f):
        f.write(f"BankAccount|{self.account_number}|{self.owner}|{self._balance}\n")

