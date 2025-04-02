import uuid
from datetime import datetime

class BankAccount:
    def __init__(self, customer_id, balance=0.0):
        self.account_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.balance = balance
        self.created_at = datetime.now()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'customer_id': self.customer_id,
            'balance': self.balance,
            'created_at': self.created_at.isoformat(),
            'type': self.__class__.__name__
        }
    
class CheckingAccount(BankAccount):
    def __init__(self, customer_id, balance=0.0, overdraft_limit=200.0):
        BankAccount.__init__(self, customer_id, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance + self.overdraft_limit < amount:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        return self.balance

    def to_dict(self):
        data = BankAccount.to_dict(self)
        data['overdraft_limit'] = self.overdraft_limit
        return data
    
class SavingsAccount(BankAccount):
    def __init__(self, customer_id, balance=0.0, interest_rate=0.02):
        BankAccount.__init__(self, customer_id, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def to_dict(self):
        data = BankAccount.to_dict(self)
        data['interest_rate'] = self.interest_rate
        return data

