class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance, defaulting to zero
        self.__account_balance = initial_balance

    def deposit(self, amount):
        # Add the specified amount to the balance
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Deduct the amount from the balance if funds are sufficient
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawn: {amount}")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        # Display the current account balance
        print(f"Current balance: {self.__account_balance}")
