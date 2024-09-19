class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    
    def value(self):
        if self.number > 10:
            return 10
        else:
            return self.number

    def is_number(self, number):
        return self.number == number

    def __str__(self):
        nums = [1,2,3,4,5,6,7,8,9,10,"J", "Q", "K"]
        return f"{nums[self.number - 1]}{self.suit[0]}"