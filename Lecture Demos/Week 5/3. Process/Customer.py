from Account import Account

class Customer:
    def __init__(self) -> None:
        self.account = Account()

    def use(self):
        if self.account != None:
            self.account.use()

if __name__ == "__main__":
    Customer().use()