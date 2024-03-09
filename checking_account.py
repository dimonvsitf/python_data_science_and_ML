from bank.bank_account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, acct_num, balance, o_draft):
        super().__init__(acct_num, balance)
        self.overdraft = o_draft


    def withdraw_funds(self, amount):
        
        if amount <= self.balance:
            self.balance = self.balance - amount 
            print(f"Successful withdrawal, current balance {self.balance}, current overdraft {self.overdraft}")
        else:  # The amount to withdraw is greater than the balance 
            deficit = amount - self.balance 
        
            if deficit <= self.overdraft: 
                self.balance = 0
                self.overdraft = self.overdraft - deficit 
                print(f"Successful withdrawal, current balance {self.balance}, current overdraft {self.overdraft}")
            else:
                print("Error: Insufficient Funds!")
            
    def get_overdraft(self):
        return self.overdraft