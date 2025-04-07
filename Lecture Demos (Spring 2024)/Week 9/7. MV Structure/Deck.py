from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for i in range(1, 14):
                self.cards.append(Card(suit, i))
    
    def get_random(self):
        return random.choice(self.cards)