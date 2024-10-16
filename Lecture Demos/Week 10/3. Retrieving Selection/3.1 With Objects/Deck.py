from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        for suit in suits:
            for i in range(1, 4):
                self.cards.append(Card(i, suit))
    
    def __str__(self):
        return "I am a deck :)"