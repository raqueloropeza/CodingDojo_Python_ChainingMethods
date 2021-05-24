import sys
sys.path.append(".")
from BankAccount import *
class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self):	
        self.account.deposit(100)
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        self = other_user
        self.account_balance += amount
        return self
guido = User("Guido van Rossum", "guido@python.com", "account1")
monty = User("Monty Python", "monty@python.com")
rocky = User("Rocky Balboa", "rocky@python.com")

guido.account.deposit(100)

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance().transfer_money(rocky,50)
monty.make_deposit(200).make_deposit(300).make_withdrawal(50).make_withdrawal(50).display_user_balance()
rocky.make_deposit(500).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()
guido.display_user_balance()
