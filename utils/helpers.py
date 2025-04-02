import re

def is_valid_email(email):
    # Simple email regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_valid_phone(phone):
    # Matches (123) 456-7890 or 123-456-7890 or similar formats
    return re.match(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$", phone) is not None

def format_currency(amount):
    return "${:,.2f}".format(amount)

def get_user_input(prompt, validator=None, error_message="Invalid input."):
    while True:
        user_input = input(prompt).strip()
        if validator is None or validator(user_input):
            return user_input
        print(error_message)
