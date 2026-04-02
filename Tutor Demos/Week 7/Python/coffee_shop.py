from order import Order
from partnership_offer import PartnershipOffer

class CoffeeShop():
    def __init__(self):
        self.__requests = []
        self.__requests.append(Order("David", "4 packs of coffee, 1 large cappucino"))
        self.__requests.append(PartnershipOffer("David"))
        self.__requests.append(Order("Jenny", "5 packs of coffee, 1 medium latte, 1 medium flat white"))
        self.__requests.append(PartnershipOffer("Jenny"))
        self.__requests.append(Order("Daisy", "2 packs of coffee, 1 large latte"))
    
    def use(self):
        for request in self.__requests:
            print(request.get_request_line())
            request.handle()
    
if __name__ == "__main__":
    shop = CoffeeShop()
    shop.use()