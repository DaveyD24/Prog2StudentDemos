from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
        for suit in suits:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))
    
    def remove_card(self):
        return self.cards.pop(0)
    
    def shuffle(self):
        random.shuffle(self.cards)