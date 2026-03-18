import random

class Team:
    def __init__(self, name):
        self.__local_name = name.split()[0]
        self.__team_name = name.split()[1]
        self.__results = []
    
    def play(self):
        result = random.randint(1, 91) * (1 if random.choice([True, False]) else -1)
        self.__results.append(result)
        return result

    def best(self):
        #No checks
        highest = float('-inf')
        for result in self.__results:
            if result > highest:
                highest = result
        return highest

    def worst(self):
        #No checks
        smallest = float('inf')
        for result in self.__results:
            if result < smallest:
                smallest = result
        return smallest
    
    def average(self):
        total = 0
        for result in self.__results:
            total += result
        return total/len(self.__results)

    def __str__(self):
        return f"{self.__local_name} {self.__team_name}"