from Deck import Deck
from Hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    def draw_card(self, deck):
        card = deck.remove_card()
        self.hand.add(card)
        if self.hand.is_busted():
            print(f"{self.name} busts with {self.hand}!")
    
    def have_turn(self, deck):
        while not self.hand.is_busted() and  ((choice := self.read_choice()) != 's'):
            if choice == 'd':
                self.draw_card(deck)
            else:
                self.help()
    
    def read_choice(self):
        self.show_hand()
        return input("Choice (d/s): ")

    def show_hand(self):
        print(self.__str__())

    def help(self):
        print("Player menu:\nd = draw a card\ns = sit")
    
    def settle(self, hand):
        if self.hand.is_better_than(hand):
            print(f"{self.name} wins with {self.hand}")
        else:
            print(f"{self.name} loses with {self.hand}" )

    def __str__(self):
        return f"{self.name} has {self.hand}"