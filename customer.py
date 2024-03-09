from bank.bank_account import BankAccount
from bank.checking_account import CheckingAccount

class Customer:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def print_accounts_report(self):
        print(f"Customer Name: {self.name}")

        for account in self.accounts:
            if isinstance(account, CheckingAccount):
                account_type = "Checking Account"
            elif isinstance(account, BankAccount):
                account_type = "Regular Account"
            else:
                print("Error: Unknown Account Type!")
            print(f"Account Type: {account_type}, Account Number: {account.account_number}, Balance: {account.balance}")

    