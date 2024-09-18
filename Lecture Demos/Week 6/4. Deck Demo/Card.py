class Card:
    def __init__(self, number, suit) -> None:
        self.number = number
        self.suit = suit



    def __str__(self):
        ids = [1,2,3,4,5,6,7,8,9,10,"Jack", "Queen", "King"]
        return f"{ids[self.number - 1]} of {self.suit}"
