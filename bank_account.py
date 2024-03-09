class BankAccount:

    def __init__(self, acct_num, balance):
        self.balance = balance
        self.account_number = acct_num

    def withdraw_funds(self, amount):
        
        if amount <= self.balance:
            self.balance = self.balance - amount 
            print(f"Successful withdrawal, current balance {self.balance}")
        else:
            print("Error: Insufficient Funds!")
    
    
    def deposit_funds(self, amount):
        
        if amount > 0:
            self.balance = self.balance + amount 
            print(f"Successful deposit, current balance {self.balance}")
        else:
            print("Error: Invalid Amount!")
    
    def get_balance(self):
        return self.balance