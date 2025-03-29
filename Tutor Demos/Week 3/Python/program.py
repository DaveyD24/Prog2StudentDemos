class Program:
    def __init__(self):
        self.names = []

    def use(self):
        #Merged read-loop pattern
        name = ""
        while (name := input("Name: ")) != 'X':
            self.names.append(name)
        print("All data validated." if self.no_emails() else "Email Spotted!")

    #None pattern
    def no_emails(self):
        for name in self.names:
            if self.is_email(name):
                return False
        return True

    #TODO: Check if equivalent python pattern
    def is_email(self, name):
        return "@" in name

if __name__ == "__main__":
    Program().use()