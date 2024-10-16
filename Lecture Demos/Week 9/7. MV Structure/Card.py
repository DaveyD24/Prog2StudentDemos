class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __str__(self):
        return f"{self.number} of {self.suit}"