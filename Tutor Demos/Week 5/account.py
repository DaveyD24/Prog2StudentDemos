class Account:
    def __init__(self, type):
        self.type = type
        self.balance = float(input(f"Initial {self.type} balance: $"))

    def has(self, amount):
        return self.balance >= amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer_to(self, amount, target):
        self.balance += amount
        target.withdraw(amount)

    def __str__(self):
        return f"{self.type} account has ${self.balance:.2f}"
