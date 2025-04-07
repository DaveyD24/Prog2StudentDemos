import random
from Card import Card

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        for suit in suits:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self):
        return self.cards.pop(0)