class Album:
    def __init__(self, name, artist, stock, price, image_url):
        self.name = name
        self.artist = artist
        self.stock = stock
        self.price = price
        self.image_url = image_url

        self.sold = 0
        self.profit = 0

    def sell(self):
        self.stock -= 1
        self.sold += 1
        self.profit = self.sold * self.price

    def __str__(self):
        return f"{self.name} by {self.artist} (${self.price})"
