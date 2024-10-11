import sys
from bank_account import BankAccount

# Create an instance of BankAccount
account = BankAccount()

# Example operations based on command line arguments
if len(sys.argv) < 2:
    print("Usage: python3 main-0.py <operation> [amount]")
    sys.exit(1)

operation = sys.argv[1].lower()

if operation == "deposit" and len(sys.argv) == 3:
    amount = float(sys.argv[2])
    if account.deposit(amount):
        print(f"Deposited: {amount}")
    else:
        print("Invalid deposit amount.")
        
elif operation == "withdraw" and len(sys.argv) == 3:
    amount = float(sys.argv[2])
    if account.withdraw(amount):
        print(f"Withdrew: {amount}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")

elif operation == "balance":
    account.display_balance()

else:
    print("Invalid operation. Use 'deposit', 'withdraw', or 'balance'.")
