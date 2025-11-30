# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)  # Ensure it's a float

    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self, amount):
        if self.account_balance >= float(amount):
            self.account_balance -= float(amount)
            return True
        else:
            return False

    def display_balance(self):
        # Format balance with 2 decimal places
        print(f"Current Balance: ${self.account_balance:.2f}")
