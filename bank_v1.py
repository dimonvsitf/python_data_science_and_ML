
balance = 20000

def withdraw_funds(amount):
    global balance
    if amount <= balance:
        balance = balance - amount 
        print(f"Successful withdrawal, current balance {balance}")
    else:
        print("Error: Insufficient Funds!")


def deposit_funds(amount):
    global balance
    if amount > 0:
        balance = balance + amount 
        print(f"Successful deposit, current balance {balance}")
    else:
        print("Error: Invalid Amount!")

def get_balance():
    global balance
    return balance 



