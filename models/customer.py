import uuid
from datetime import datetime

class Customer:
    def __init__(self, first_name, last_name, address, email, phone):
        self.customer_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.created_at = datetime.now()
        self.accounts = []  # List of account IDs

    def add_account(self, account):
        self.accounts.append(account.account_id)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at.isoformat(),
            "accounts": self.accounts
        }
