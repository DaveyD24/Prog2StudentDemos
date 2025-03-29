from account import Account

class Customer:
    def __init__(self):
        self.accounts = []

    def use(self):
        choice = ''
        while (choice := input("Customer menu (a/r/d/w/s/x): ")) != 'x':
            if choice == 'a':
                self.add()
            elif choice =='r':
                self.remove()
            elif choice == 'd':
                self.deposit()
            elif choice == 'w':
                self.withdraw()
            elif choice == 's':
                self.show()
            else:
                self.help()
        print("Done")

    #Not strictly necessary in python, but a very reused and error prone piece of code
    #Good to have only 1 instance of it
    def read_amount(self, action):
        return float(input(f"Amount to {action}: $"))

    def account(self, type):
        for acc in self.accounts:
            if acc.is_type(type):
                return acc
        return None

    def add(self):
        type = input("Account type: ")
        acc = self.account(type)
        if acc == None:
            self.accounts.append(Account(type))
        else:
            print("Account already exists!")

    def remove(self):
        type = input("Account type: ")
        acc = self.account(type)
        if acc != None:
            self.accounts.remove(acc)
        else:
            print("No such account!")

    def deposit(self):
        type = input("Account type: ")
        acc = self.account(type)
        if acc != None:
            amount = self.read_amount("deposit")
            acc.deposit(amount)
        else:
            print("No such account!")

    def withdraw(self):
        type = input("Account type: ")
        acc = self.account(type)
        if acc != None:
            amount = self.read_amount("withdraw")
            if acc.has(amount):
                acc.withdraw(amount)
            else:
                print("Insufficient funds")
        else:
            print("No such account!")

    def show(self):
        for account in self.accounts:
            print(account.__str__())

    def help(self):
        print("Menu options")
        print("a = add")
        print("r = remove")
        print("d = deposit")
        print("w = withdraw")
        print("s = show")
        print("x = exit")

if __name__ == "__main__":
    Customer().use()