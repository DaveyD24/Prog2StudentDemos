class Account:
    def __init__(self, type) -> None:
        self.type = type
        self.balance = self.read_balance()
    
    def read_balance(self):
        return float(input(f"Initial {self.type} balance: $"))
    
    def has(self, amount):
        return self.balance >= amount

    def has_type(self, type):
        return self.type == type

    def read_choice(self):
        return input("Choice: (d/w/v/x): ")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def __str__(self):
        return f"{self.type} account has ${self.balance:.2f}"