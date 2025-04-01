# Python OOP Mini-Project: Banking System Case Study

## Project Overview

This is a Python-based object-oriented programming (OOP) mini-project simulating a simplified **Banking System**. The goal is to model a real-world banking environment that includes customers, employees, accounts, and services such as loans and credit cards — all using core OOP principles.

## Features

- Modeled with Python classes and OOP design patterns
- Supports:
  - Creating customer and employee records
  - Opening and managing accounts (checking, savings)
  - Deposits, withdrawals, and balance inquiries
  - Loan and credit card service management
- CLI-based user interaction
- Customizable backend storage (CSV, JSON, or database)

## Project Structure
```
banking-system/
├── main.py                  # Entry point: handles CLI interaction
│
├── models/                  # Core classes for business logic (OOP)
│   ├── customer.py          # Customer class (name, address, accounts, etc.)
│   ├── account.py           # Base Account class (with savings/checking subclasses)
│   ├── employee.py          # Optional: employee access or management
│   └── service.py           # Loan, credit card, or other banking services
│
├── data/                    # Data storage (flexible backend)
│   ├── customers.json       # Sample persistent storage (could also support CSV/DB)
│   └── transactions.json    # Optional: store deposits/withdrawals
│
├── logs/                    # Logging directory
│   └── app.log              # Log info, warnings, errors (via logging module)
│
├── utils/                   # Helper functions, config, validation, etc.
│   ├── helpers.py           # Shared logic: formatters, validations
│   └── storage.py           # Optional: wrap JSON/CSV read/write logic
│
├── tests/                   # Unit tests
│   ├── test_accounts.py     # Unit tests for Account logic
│   └── test_customers.py    # Unit tests for Customer functionality
│
├── UML_Diagram.png          # Class structure and relationships
├── README.md                # Project description, usage, features
└── .gitignore               # Files/folders to exclude from Git tracking
```

## Key Concepts Demonstrated

- Python **OOP** design (`class`, `inheritance`, `encapsulation`)
- **Exception handling** for graceful user experience
- **Logging** with timestamps to a `logs/app.log` file
- Modular and reusable **code structure**
- Follows **PEP-8** guidelines and uses **docstrings**
- Data persistence through external files (e.g., **JSON** or **CSV**)

## How to Run

1. Clone the repository:

<pre>
```bash
git clone https://github.com/yourusername/banking-system.git
cd banking-system
Run the CLI program:
```
</pre>
2. Run the CLI program:
<pre>
```bash
python main.py
```
</pre>