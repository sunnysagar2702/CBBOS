# Define a class for a generic bank account.
class BankAccount:
    # Constructor to initialize account attributes.
    def __init__(self, account_number, account_holder):
        self.account_number = account_number  # Store the account number.
        self.account_holder = account_holder  # Store the account holder's name.
        self.balance = 0.0  # Initialize the account balance to 0.0.
        self.transactions = []  # Initialize an empty list to store transactions.

    # Method to deposit money into the account.
    def deposit(self, amount):
        if amount > 0:  # Check if the deposit amount is positive.
            self.balance += amount  # Increase the balance by the deposit amount.
            self.transactions.append(f"Deposit: +INR{amount:.2f}")  # Record the transaction.
            return True  # Return True to indicate a successful deposit.
        return False  # Return False if the deposit amount is non-positive.

    # Method to withdraw money from the account.
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:  # Check if withdrawal is valid.
            self.balance -= amount  # Decrease the balance by the withdrawal amount.
            self.transactions.append(f"Withdrawal: -INR{amount:.2f}")  # Record the transaction.
            return True  # Return True to indicate a successful withdrawal.
        return False  # Return False if the withdrawal is invalid.

    # Method to get the current balance of the account.
    def get_balance(self):
        return self.balance  # Return the current balance.

    # Method to get the transaction history of the account.
    def get_transactions(self):
        return self.transactions  # Return the list of transactions.

    # Method to transfer funds from this account to the target account.
    def transfer(self, target_account, amount):
        if amount > 0 and self.balance >= amount:  # Check if the transfer is valid.
            self.balance -= amount  # Decrease the sender's balance.
            target_account.balance += amount  # Increase the receiver's balance.
            # Record the transaction for both accounts.
            self.transactions.append(f"Transfer to {target_account.account_number}: -INR{amount:.2f}")
            target_account.transactions.append(f"Transfer from {self.account_number}: +INR{amount:.2f}")
            return True  # Return True to indicate a successful transfer.
        return False  # Return False if the transfer is invalid.

# Define a class for a savings account that inherits from BankAccount.
class SavingsAccount(BankAccount):
    # Constructor to initialize savings account attributes.
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)  # Initialize parent attributes.
        self.interest_rate = 0.02  # Set the interest rate for savings accounts.

    # Method to apply interest to the savings account balance.
    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate  # Calculate interest amount.
        self.balance += interest_amount  # Add interest to the balance.

# Define a class for a current account that inherits from BankAccount.
class CurrentAccount(BankAccount):
    # Constructor to initialize current account attributes.
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)  # Initialize parent attributes.
        self.overdraft_limit = 1000.0  # Set the overdraft limit for current accounts.

    # Method to implement overdraft protection for the current account.
    def overdraft_protection(self):
        if self.balance < 0 and abs(self.balance) <= self.overdraft_limit:
            self.balance = 0  # Apply overdraft protection if conditions are met.
            return True
        return False

# Function to generate a unique account number.
def generate_account_number(accounts):
    counter = len(accounts) + 1  # Calculate a unique account number using a counter.
    return str(100000 + counter)  # Return a unique account number as a string.

# Function to create a new bank account and add it to the accounts dictionary.
def create_account(accounts):
    account_holder = input("Enter account holder name: ")  # Get account holder name from user.
    account_type = input("Enter account type (Savings or Current): ").lower()  # Get account type from user.
    
    # Check the account type and create the appropriate account.
    if account_type == "savings":
        account_number = generate_account_number(accounts)  # Generate a unique account number.
        accounts[account_number] = SavingsAccount(account_number, account_holder)  # Create a savings account.
        print(f"Account created with account number: {account_number}")  # Print a confirmation message.
    elif account_type == "current":
        account_number = generate_account_number(accounts)  # Generate a unique account number.
        accounts[account_number] = CurrentAccount(account_number, account_holder)  # Create a current account.
        print(f"Account created with account number: {account_number}")  # Print a confirmation message.
    else:
        print("Invalid account type.")  # Print an error message for an invalid account type.

# Function to deposit money into an account.
def deposit(accounts):
    account_number = input("Enter account number: ")  # Get account number from user.
    amount = float(input("Enter deposit amount: "))  # Get deposit amount from user.
    
    # Check if the account exists and deposit the money if valid.
    if account_number in accounts and accounts[account_number].deposit(amount):
        print("Deposit successful.")  # Print a success message.
    else:
        print("Invalid account or deposit amount.")  # Print an error message.

# Function to withdraw money from an account.
def withdraw(accounts):
    account_number = input("Enter account number: ")  # Get account number from user.
    amount = float(input("Enter withdrawal amount: "))  # Get withdrawal amount from user.
    
    # Check if the account exists and withdraw the money if valid.
    if account_number in accounts and accounts[account_number].withdraw(amount):
        print("Withdrawal successful.")  # Print a success message.
    else:
        print("Invalid account or insufficient balance.")  # Print an error message.

# Function to check the balance and display transaction history of an account.
def balance_inquiry(accounts):
    account_number = input("Enter account number: ")  # Get account number from user.
    
    # Check if the account exists and retrieve balance and transaction history if valid.
    if account_number in accounts:
        balance = accounts[account_number].get_balance()  # Get the account balance.
        print(f"Account balance: INR{balance:.2f}")  # Print the account balance.
        transactions = accounts[account_number].get_transactions()  # Get transaction history.
        if transactions:
            print("\nTransaction History:")  # Print a header for transaction history.
            for transaction in transactions:
                print(transaction)  # Print each transaction.
    else:
        print("Invalid account.")  # Print an error message for an invalid account.

# Function to transfer funds between two accounts.
def fund_transfer(accounts):
    sender_account_number = input("Enter your account number: ")  # Get sender's account number.
    
    # Check if the sender's account exists.
    if sender_account_number in accounts:
        sender_account = accounts[sender_account_number]  # Get sender's account object.
        receiver_account_number = input("Enter the receiver's account number: ")  # Get receiver's account number.
        
        # Check if the receiver's account exists.
        if receiver_account_number in accounts:
            receiver_account = accounts[receiver_account_number]  # Get receiver's account object.
            amount = float(input("Enter the amount to transfer: "))  # Get the transfer amount.
            
            # Check if the transfer is valid and perform the transfer.
            if sender_account.transfer(receiver_account, amount):
                print("Fund transfer successful.")  # Print a success message.
            else:
                print("Invalid amount or insufficient balance.")  # Print an error message.
        else:
            print("Receiver's account does not exist.")  # Print an error message.
    else:
        print("Sender's account does not exist.")  # Print an error message.

# Function to manage the main program flow.
def main():
    accounts = {}  # Initialize an empty dictionary to store accounts.

    while True:  # Start an infinite loop for user interaction.
        print("\n===== Banking Operations =====")  # Print a menu header.
        print("1. Create Account")  # Display the option to create an account.
        print("2. Deposit")  # Display the option to deposit money.
        print("3. Withdraw")  # Display the option to withdraw money.
        print("4. Balance Inquiry")  # Display the option to check balance and transaction history.
        print("5. Fund Transfer")  # Display the option to transfer funds.
        print("6. Exit")  # Display the option to exit the program.
        choice = input("Enter your choice: ")  # Get the user's choice.

        if choice == "1":
            create_account(accounts)  # Call the create_account function.
        elif choice == "2":
            deposit(accounts)  # Call the deposit function.
        elif choice == "3":
            withdraw(accounts)  # Call the withdraw function.
        elif choice == "4":
            balance_inquiry(accounts)  # Call the balance_inquiry function.
        elif choice == "5":
            fund_transfer(accounts)  # Call the fund_transfer function.
        elif choice == "6":
            print("Exiting the program.")  # Print an exit message.
            break  # Exit the program by breaking out of the loop.

if __name__ == "__main__":
    main()  # Call the main function to start the program.

