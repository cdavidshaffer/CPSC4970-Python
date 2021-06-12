class Bank:
    def __init__(self):
        self._accounts = []
        self._current_account_number = 0

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, ba):
        self._accounts.append(ba)

    def remove_account(self, ba):
        self._accounts.remove(ba)

    def get_account_by_id(self, account_number):
        possibles = [acct for acct in self._accounts if acct.account_number == account_number]
        if len(possibles) == 0:
            return None
        else:
            return possibles[0]

    def get_next_account_number(self):
        self._current_account_number += 1
        return self._current_account_number
