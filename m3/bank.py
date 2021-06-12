class Bank:
    _sole_instance = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def __init__(self):
        self._accounts = []

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, account):
        self._accounts.append(account)


if __name__ == '__main__':
    from bank_account import BankAccount
    b = Bank.instance()
    b.add_account(BankAccount(101, "Fred"))
    b.add_account(BankAccount(102, "Barney"))
    for a in b.accounts:
        a.print()