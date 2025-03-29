class Account:
    def __init__(self, type):
        self.type = type
        self.balance = float(input(f"Initial {self.type} balance: $"))

    def has(self, amount):
        return self.balance >= amount

    def is_type(self, type):
        return self.type == type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.type} account has ${self.balance:.2f}"