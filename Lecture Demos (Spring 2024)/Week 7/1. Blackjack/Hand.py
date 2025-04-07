from Card import Card

class Hand:
    def __init__(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def value(self):
        total = 0
        for card in self.cards:
            total += card.value()
        return total
    
    def is_busted(self):
        return self.value() > 21
    
    def is_better_than(self, other):
        return not self.is_busted() and (other.is_busted() or self.value() > other.value())

    def is_blackjack(self):
        return len(self.cards) == 2 and self.has(1) and self.value() == 21

    def has(self, number):
        for card in self.cards:
            if card.is_number(number):
                return True
        return False

    def __str__(self):
        s = ""
        for card in self.cards:
            s += card.__str__()
            s += " "
        return f"{s.strip()}: {self.value()}"