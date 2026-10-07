from model.observable import Observable

class Album(Observable):
    def __init__(self, artist, name, stock, price):
        super().__init__()
        self.__artist = artist
        self.__name = name
        self.__stock = stock
        self.__price = price

        self.__sold = 0

    def sell(self):
        self.__stock -= 1
        self.__sold += 1
        self.notify()
    
    def get_name(self):
        return self.__name

    def get_artist(self):
        return self.__artist

    def get_sold(self):
        return self.__sold

    def get_profit(self):
        return self.__sold * self.__price

    def can_sell(self):
        return self.__stock > 0

    def __str__(self):
        return f"{self.__name} by {self.__artist} (${self.__price})"