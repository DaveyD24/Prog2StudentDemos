class Account:
    def __init__(self) -> None:
        self.balance = self.readBalance()
    
    def use(self):
        while (choice := self.readChoice()) != 'x':
            if choice == 'd':
                self.deposit()
            elif choice == 'w':
                self.withdraw()
            elif choice == 's':
                self.show()
            else:
                self.help()

    def readBalance(self):
        return float(input("Initial Balanace: $"))

    def deposit(self):
        self.balance += self.readAmount("deposit")

    def withdraw(self):
        self.balance -= self.readAmount("withdraw")

    def show(self):
        print(self.__str__())

    def readAmount(self, action):
        return float(input(f"Amount to {action}: $"))

    def readChoice(self):
        return input("Choice (d/w/s/x): ")

    def help(self):
        print("Account menu options:\nd = deposit\nw = withdraw\ns = show\nx = exit")

    def __str__(self):
        return f"Account has ${self.balance:.2f}"