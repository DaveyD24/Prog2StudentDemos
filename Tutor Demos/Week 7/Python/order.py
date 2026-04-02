from request import Request
class Order(Request):
    def __init__(self, name, products):
        self.__name = name
        self.__products = products
    
    def get_request_line(self):
        return f"{self.__name} has requested {self.__products}"
    
    def handle(self):
        for item in self.__products.split(","):
            print(f"Item: {item}. ")
            choice = input("Approve request? (y/n): ")
            print("Approved" if choice == "y" else "Rejected")
            