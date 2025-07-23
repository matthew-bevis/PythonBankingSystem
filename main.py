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
            
        }
