from bank import Bank
from bank_account import BankAccount
from enum import Enum, unique
import pickle


@unique
class MenuChoice(Enum):
    LIST = (1, "List accounts")
    ADD = (2, "Add account")
    DEPOSIT = (3, "Deposit")
    WITHDRAW = (4, "Withdraw")
    QUIT = (5, "Quit")

    def __init__(self, ident, description):
        self.ident = ident
        self.description = description

    def __str__(self):
        return f"{self.ident}) {self.description}"


def get_menu_choice():
    print("\n\nMain menu:")
    for choice in MenuChoice:
        print(choice)
    return MenuChoice(int(input("Select choice> ")))


def list_accounts(bank):
    print("Accounts:")
    for account in bank.accounts:
        print(f"\t{account}")


def add_account(bank):
    owner = input("Enter owner's name: ")
    ba = BankAccount(bank.get_next_account_number(), owner)
    bank.add_account(ba)
    print(ba)


def deposit(bank):
    acctno = int(input("Enter account number: "))
    ba = bank.get_account_by_id(acctno)
    amount = float(input("Enter amount to deposit: "))
    ba.deposit(amount)
    print(ba)


def withdraw(bank):
    acctno = int(input("Enter account number: "))
    ba = bank.get_account_by_id(acctno)
    amount = float(input("Enter amount to withdraw: "))
    ba.withdraw(amount)
    print(ba)


def load_bank():
    try:
        with open("bank.dat", mode="rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Bank()


def save_bank(bank):
    with open("bank.dat", mode="wb") as f:
        pickle.dump(bank, f)


def main():
    bank = load_bank()
    choice = get_menu_choice()
    while choice != MenuChoice.QUIT:
        if choice == MenuChoice.LIST:
            list_accounts(bank)
        elif choice == MenuChoice.ADD:
            add_account(bank)
        elif choice == MenuChoice.DEPOSIT:
            deposit(bank)
        elif choice == MenuChoice.WITHDRAW:
            withdraw(bank)
        save_bank(bank)
        choice = get_menu_choice()

    print("Good bye")


def demo_save():
    bank = load_bank()
    for i in range(10000):
        bank.add_account(BankAccount(bank.get_next_account_number(), str(i)))
    print("saving")
    save_bank(bank)
    print("done")


if __name__ == '__main__':
    main()