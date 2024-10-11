import json
import os

class BankAccount:
    def __init__(self):
        self.file_path = 'account_balance.json'
        self.__account_balance = 0
        self.load_balance()

    def load_balance(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.__account_balance = data.get('balance', 0)

    def save_balance(self):
        with open(self.file_path, 'w') as file:
            json.dump({'balance': self.__account_balance}, file)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            self.save_balance()  # Save the new balance
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            self.save_balance()  # Save the new balance
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: {self.__account_balance}")
