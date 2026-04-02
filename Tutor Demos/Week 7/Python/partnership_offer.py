from request import Request
class PartnershipOffer(Request):
    def __init__(self, name):
        self.__name = name
    
    def get_request_line(self):
        return f"{self.__name} has requested to do business with you"
    
    def handle(self):
        choice = input("Approve request? (y/n): ")
        print("Approved" if choice == "y" else "Rejected")