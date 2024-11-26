# Develop a class called BankAccount. It should have an account number,
# current balance and account holder. Deposit, withdraw, transfer and
# check balance methods should be implemented

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def transfer(self, amount, to_account):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            to_account.deposit(amount)

    def check_balance(self):
        return self.balance
