import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <operation> [amount]")
        return

    # Initialize a bank account with a default balance
    account = BankAccount()

    # Parse the operation from command line arguments
    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) == 3:
            amount = float(sys.argv[2])
            account.deposit(amount)
        else:
            print("Please provide an amount to deposit.")
    
    elif operation == "withdraw":
        if len(sys.argv) == 3:
            amount = float(sys.argv[2])
            account.withdraw(amount)
        else:
            print("Please provide an amount to withdraw.")

    elif operation == "balance":
        account.display_balance()

    else:
        print("Invalid operation. Use 'deposit', 'withdraw', or 'balance'.")

if __name__ == "__main__":
    main()
