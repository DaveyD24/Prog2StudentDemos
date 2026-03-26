import random

class Team:
    def __init__(self, name):
        self.__local_name = name.split()[0]
        self.__team_name = name.split()[1]
        self.__results = []
    
    def play(self, opponent):
        result = random.randint(1, 91) * (1 if random.choice([True, False]) else -1)
        self.__results.append(result)
        opponent.__results.append(result*-1)
        return result

    def has(self, substring):
        return substring.lower() in self.__local_name.lower() or substring.lower() in self.__team_name.lower()

    def best(self):
        if self.no_wins():
            return 0
        highest = float('-inf')
        for result in self.__results:
            if result > highest:
                highest = result
        return highest

    def worst(self):
        if self.no_losses():
            return 0
        smallest = float('inf')
        for result in self.__results:
            if result < smallest:
                smallest = result
        return smallest
    
    def average(self):
        if len(self.__results) == 0:
            return 0
        total = 0
        for result in self.__results:
            total += result
        return total/len(self.__results)

    def no_wins(self):
        for result in self.__results:
            if result >= 0:
                return False
        return True

    def no_losses(self):
        for result in self.__results:
            if result < 0:
                return False
        return True

    def __str__(self):
        return f"{self.__local_name} {self.__team_name}"