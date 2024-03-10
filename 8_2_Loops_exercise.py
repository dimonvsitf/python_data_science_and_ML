#!/usr/bin/env python
# coding: utf-8

# # Python Loops Exercise: Cryptocurrency Wallet Tracker
# 
# ### Exercise Description
# 
#         
# Write a Python script to simulate a simple cryptocurrency wallet tracker. Your script should:
#             
# 1. Iterate over the list of cryptocurrency transactions: [300, -500, 1000, -2000, 400, -100, 700, -50].
# 2. For each deposit (positive amount), add it to the wallet balance and print "Deposit processed: [amount]"
# 3. For each withdrawal (negative amount), check if the wallet balance is sufficient. If so, subtract it from the balance; otherwise, print "Insufficient funds for this withdrawal: [amount]" and terminate the loop.
# 4. After each transaction, print the current wallet balance.
# 
# The initial wallet balance is 1000. Aim to provide clear output showing each transaction's processing and the wallet balance update.
#         
# ### Expected Output
# 
# An example of expected output (not exhaustive):
# 
# Deposit processed: 300
# Current balance: 1300
# ...
# Insufficient funds for this withdrawal: -2000
#         
# Hints
#         
# Use a for loop to iterate over the list. Utilize if statements to differentiate between deposits and withdrawals. The break statement will help you exit the loop when the balance is insufficient.
# 

# In[17]:


balance = 1000
str_input = input('Starting balance is 1000. Provide a list of cryptocurrency transactions. e.g.[300, -500, 1000, -2000, 400, -100, 700, -50]')

try:
    transactions = [ int(item) for item in str_input.strip("[]").split(", ") ]
except ValueError:
    print("invalid file format.Please ensure you're entering a list of numbers separated by commas.")
    transactions = []

# type(transactions[0])

for order in transactions: 
    if order >= 0:
        balance += order
        print (f'Deposit of {order} is processed. New balance: {balance}')
    else: 
        delta = balance + order
        if delta >=0:
            balance += order
            print(f'Withdrawal of {order} is processed. New balance: {balance}')
        else: 
            print(f"Insufficient funds for this withdrawal: {order}. Current balance is {balance}")
            break

