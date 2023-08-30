# CBBOS
Console Based Banking Operations System

This Python program provides a simple bank account management system with the following features:

- Create Savings and Current accounts.
- Deposit money into an account.
- Withdraw money from an account.
- Check the account balance and view transaction history.
- Transfer funds between two accounts.

## How to Use

1. Run the program by executing the `main()` function at the end of the code.
2. You will be presented with a menu of banking operations.
3. Choose the operation you want to perform by entering the corresponding number.
4. Follow the on-screen instructions to complete the chosen operation.

## Classes

### `BankAccount`

This is the base class for all bank accounts. It includes the following methods:

- `deposit(amount)`: Deposit money into the account.
- `withdraw(amount)`: Withdraw money from the account.
- `get_balance()`: Get the current balance of the account.
- `get_transactions()`: Get the transaction history of the account.
- `transfer(target_account, amount)`: Transfer funds from this account to the target account.

### `SavingsAccount` (Inherits from `BankAccount`)

This class represents a savings account and includes an additional method:

- `apply_interest()`: Apply interest to the savings account balance.

### `CurrentAccount` (Inherits from `BankAccount`)

This class represents a current account and includes an additional method:


## Functions

- `generate_account_number(accounts)`: Generate a unique account number.
- `create_account(accounts)`: Create a new bank account and add it to the accounts dictionary.
- `deposit(accounts)`: Deposit money into an account.
- `withdraw(accounts)`: Withdraw money from an account.
- `balance_inquiry(accounts)`: Check the balance of an account and display transaction history.
- `fund_transfer(accounts)`: Transfer funds between two accounts.
- `main()`: The main program loop that allows users to interact with the banking system.


### Usage
Run the script and follow the on-screen prompts to perform banking operations.

## How to Run
1. Make sure you have Python installed on your system.
2. Save this script to a file, e.g., `CBBOS_Project.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the command: `python CBBOS_Project.py`





## Example Usage

```python
if __name__ == "__main__":
    main()
