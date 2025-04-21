class Album:
    def __init__(self, artist, name, stock, price):
        self.artist = artist
        self.name = name
        self.stock = stock
        self.price = price

        self.sold = 0
        self.profit = 0

    def sell(self):
        self.stock -= 1
        self.sold += 1
        self.profit = self.sold * self.price
