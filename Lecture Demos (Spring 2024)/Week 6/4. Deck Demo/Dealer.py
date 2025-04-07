from Deck import Deck

class Dealer:
    def __init__(self) -> None:
        self.deck = Deck()

    def use(self):
        while(choice := self.read_choice()) != 'x':
            if choice == 's':
                self.shuffle()
            elif choice == 'd':
                self.deal()
    
    def read_choice(self):
        return input("Choice (s/d/x): ")

    def shuffle(self):
        self.deck.shuffle()
        print("Deck has been shuffled")
        pass

    def deal(self):
        card = self.deck.remove_card()
        print(card)
        pass

if __name__ == "__main__":
    Dealer().use()