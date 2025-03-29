from account import Account

class Customer:
    def __init__(self):
        self.savings_account = Account("Savings")
        self.loan_account = Account("Loan")

    def use(self):
        choice = ''
        while (choice := input("Customer menu (d/w/t/s/x): ")) != 'x':
            if choice == 'd':
                self.deposit()
            elif choice == 'w':
                self.withdraw()
            elif choice == 't':
                self.transfer()
            elif choice == 's':
                self.show()
            else:
                self.help()
        print("Done")

    #Not strictly necessary in python, but a very reused and error prone piece of code
    #Good to have only 1 instance of it
    def read_amount(self, action):
        return float(input(f"Amount to {action}: $"))

    def deposit(self):
        amount = self.read_amount("deposit")
        self.savings_account.deposit(amount)

    def withdraw(self):
        amount = self.read_amount("withdraw")
        if self.savings_account.has(amount):
            self.savings_account.withdraw(amount)
        else:
            print("Insufficient funds")

    def transfer(self):
        amount = self.read_amount("withdraw")
        if self.savings_account.has(amount):
            self.savings_account.transfer_to(amount, self.loan_account)
        else:
            print("Insufficient funds")

    def show(self):
        print(self.savings_account.__str__())
        print(self.loan_account.__str__())

    def help(self):
        print("Menu options")
        print("d = deposit")
        print("w = withdraw")
        print("t = transfer")
        print("s = show")
        print("x = exit")

if __name__ == "__main__":
    Customer().use()