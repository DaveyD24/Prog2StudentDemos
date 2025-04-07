from Deck import Deck
from Player import Player
from Hand import Hand

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.players = []
        self.players.append(Player("David"))
        self.players.append(Player("Angela"))
    
    def use(self):
        self.shuffle()
        self.deal()
        self.deal()
        for player in self.players:
            player.have_turn(self.deck)
        self.have_turn()
        self.settle()

    def read_choice(self):
        return input("Choice (d/s): ")

    def deal(self):
        for player in self.players:
            player.draw_card(self.deck)
        self.draw_card()

    def draw_card(self):
        self.hand.add(self.deck.remove_card())
        if self.hand.is_busted():
            print(f"Dealer bust with {self.hand}!")

    def have_turn(self):
        while not self.hand.is_busted():
            self.draw_card()

    def shuffle(self):
        self.deck.shuffle()

    def settle(self):
        self.show_hand()
        for player in self.players:
            player.settle(self.hand)
    
    def show_hand(self):
        print(f"Dealer has {self.hand}")

if __name__ == "__main__":
    Dealer().use()