class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        # Deposit money into the account
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +INR{amount:.2f}")
            return True
        return False

    def withdraw(self, amount):
        # Withdraw money from the account
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -INR{amount:.2f}")
            return True
        return False

    def get_balance(self):
        # Get the current balance of the account
        return self.balance

    def get_transactions(self):
        # Get the transaction history of the account
        return self.transactions

    def transfer(self, target_account, amount):
        # Transfer funds from this account to the target account
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f"Transfer to {target_account.account_number}: -INR{amount:.2f}")
            target_account.transactions.append(f"Transfer from {self.account_number}: +INR{amount:.2f}")
            return True
        return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.interest_rate = 0.02

    def apply_interest(self):
        # Apply interest to the savings account balance
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = 1000.0

    def overdraft_protection(self):
        # Implement overdraft protection for the current account
        if self.balance < 0 and abs(self.balance) <= self.overdraft_limit:
            self.balance = 0
            return True
        return False

def generate_account_number(accounts):
    # Generate a unique account number using a counter.
    counter = len(accounts) + 1
    return str(100000 + counter)

def create_account(accounts):
    # Create a new bank account and add it to the accounts dictionary
    account_holder = input("Enter account holder name: ")
    account_type = input("Enter account type (Savings or Current): ").lower()
    if account_type == "savings":
        account_number = generate_account_number(accounts)
        accounts[account_number] = SavingsAccount(account_number, account_holder)
        print(f"Account created with account number: {account_number}")
    elif account_type == "current":
        account_number = generate_account_number(accounts)
        accounts[account_number] = CurrentAccount(account_number, account_holder)
        print(f"Account created with account number: {account_number}")
    else:
        print("Invalid account type.")

def deposit(accounts):
    # Deposit money into an account
    account_number = input("Enter account number: ")
    amount = float(input("Enter deposit amount: "))
    if account_number in accounts and accounts[account_number].deposit(amount):
        print("Deposit successful.")
    else:
        print("Invalid account or deposit amount.")

def withdraw(accounts):
    # Withdraw money from an account
    account_number = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))
    if account_number in accounts and accounts[account_number].withdraw(amount):
        print("Withdrawal successful.")
    else:
        print("Invalid account or insufficient balance.")

def balance_inquiry(accounts):
    # Check the balance of an account and display transaction history
    account_number = input("Enter account number: ")
    if account_number in accounts:
        balance = accounts[account_number].get_balance()
        print(f"Account balance: INR{balance:.2f}")
        transactions = accounts[account_number].get_transactions()
        if transactions:
            print("\nTransaction History:")
            for transaction in transactions:
                print(transaction)
    else:
        print("Invalid account.")

def fund_transfer(accounts):
    # Transfer funds between two accounts
    sender_account_number = input("Enter your account number: ")
    if sender_account_number in accounts:
        sender_account = accounts[sender_account_number]
        receiver_account_number = input("Enter the receiver's account number: ")
        if receiver_account_number in accounts:
            receiver_account = accounts[receiver_account_number]
            amount = float(input("Enter the amount to transfer: "))
            if sender_account.transfer(receiver_account, amount):
                print("Fund transfer successful.")
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("Receiver's account does not exist.")
    else:
        print("Sender's account does not exist.")

def main():
    accounts = {}

    while True:
        print("\n===== Banking Operations =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Inquiry")
        print("5. Fund Transfer") 
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            balance_inquiry(accounts)
        elif choice == "5":
            fund_transfer(accounts) 
        elif choice == "6":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
