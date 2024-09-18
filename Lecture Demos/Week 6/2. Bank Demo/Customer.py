from Account import Account

class Customer:
    def __init__(self) -> None:
        self.accounts = []

    def use(self):
        while (choice := self.read_choice()) != 'x':
            if choice == 'a':
                self.add()
            elif choice == 'r':
                self.remove()
            elif choice == 'd':
                self.deposit()
            elif choice == 'w':
                self.withdraw()
            elif choice == 'v':
                self.view()
            else:
                self.help()

    def read_choice(self):
        return input("Choice (a/r/d/w/v/x): ")

    def read_type(self):
        return input("Account type: ")

    def account(self, type):
        for account in self.accounts:
            if account.has_type(type):
                return account
        return None

    def add(self):
        type = self.read_type()
        acc = self.account(type)
        if acc != None:
            print("Account already exists")
        else:
            self.accounts.append(Account(type))

    def remove(self):
        type = self.read_type()
        acc = self.account(type)
        if acc == None:
            print("No such account")
        else:
            self.accounts.remove(acc)

    def deposit(self):
        acc = self.account(self.read_type())
        if acc != None:
            amount = self.read_amount()
            acc.deposit(amount)
        else:
            print("No such account")
    
    def withdraw(self):
        acc = self.account(self.read_type())
        if acc != None:
            amount = self.read_amount()
            if acc.has(amount):
                acc.withdraw(amount)
            else:
                print("Not enough money in account")
        else:
            print("No such account")

    def read_amount(self):
        return float(input("Amount: "))
    
    def view(self):
        for account in self.accounts:
            print(account)

if __name__ == "__main__":
    Customer().use()