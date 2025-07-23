#!/bin/bash

import json
import os
import logging
from datetime import datetime

#Logging utility
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename='logs/bank.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

#File storage utility
df = 'data/customers.json'
os.makedirs('data', exist_ok=True)

#Function that loads stored data from JSON
def load_data():
    try:
        if os.path.exists(df):
            with open(df, 'r') as file:
                return json.load(file)
        return []
    except Exception as e:
        logging.error(f'Failed to load data: {e}')
        return []
    
def save_data(data):
    try:
        with open(df, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f'Failed to save data: {e}')

class BankAccount:
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 0.0

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            logging.info(f'Withdrew ${amount:.2f} to {self.account_type} account.')
        else:
            raise ValueError('Withdrawal amount must be a positive number and not exceed account balance')
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            logging.info(f'Deposited ${amount:.2f} to {self.account_type} account.')
        else:
            raise ValueError('Deposit amount must be a positive number')
    
    def to_dict(self):
        return {'account_type': self.account_type, "balance": self.balance} 


class Customer:
    def __init__(self, fName, lName, addr):
        self.customer_id = f'C{int(datetime.now().timestamp())}'
        self.fName = fName
        self.lName = lName
        self.addr = addr
        self.accounts = []

    def add_account(self, account_type):
        self.accounts.append(BankAccount(account_type))

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'first_name': self.fName,
            'last_name': self.lName,
            'address': self.addr,
            'accounts': [a.to_dict() for a in self.accounts]
        }


#CLI

def main():
    data = load_data()
    customers = [Customer(**{k: v for k, v in c.items() if k != 'accounts'}) for c in data]

    for c, stored in zip(customers, data):
        for a in stored['accounts']:
            account = BankAccount(a['account_type'])
            account.balance = a['balance']
            c.accounts.append(account)

    print("Welcome to the CLI Banking System")
    while True:
        print("\nOptions:\n1. Add Customer\n2. Deposit\n3. Withdraw\n4. Show Customers\n5. Exit")
        choice = input("Select: ")

        try:
            if choice == '1':
                fn = input("First Name: ")
                ln = input("Last Name: ")
                addr = input("Address: ")
                acc_type = input("Account Type (checking/savings): ")
                customer = Customer(fn, ln, addr)
                customer.add_account(acc_type)
                customers.append(customer)
                logging.info(f"Added customer {fn} {ln}")

            elif choice == '2':
                cid = input("Customer ID: ")
                amt = float(input("Amount to deposit: "))
                acc_type = input("Account Type: ")
                customer = next((c for c in customers if c.customer_id == cid), None)
                if customer:
                    acc = next((a for a in customer.accounts if a.account_type == acc_type), None)
                    if acc:
                        acc.deposit(amt)
                    else:
                        print("Account not found.")
                else:
                    print("Customer not found.")

            elif choice == '3':
                cid = input("Customer ID: ")
                amt = float(input("Amount to withdraw: "))
                acc_type = input("Account Type: ")
                customer = next((c for c in customers if c.customer_id == cid), None)
                if customer:
                    acc = next((a for a in customer.accounts if a.account_type == acc_type), None)
                    if acc:
                        acc.withdraw(amt)
                    else:
                        print("Account not found.")
                else:
                    print("Customer not found.")

            elif choice == '4':
                for c in customers:
                    print(f"{c.customer_id} - {c.first_name} {c.last_name} - {c.address}")
                    for a in c.accounts:
                        print(f"   {a.account_type} - Balance: ${a.balance:.2f}")

            elif choice == '5':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")
            logging.warning(f"Operation failed: {e}")

    save_data([c.to_dict() for c in customers])
    print("Thank you for using the banking system.")

if __name__ == '__main__':
    main()
