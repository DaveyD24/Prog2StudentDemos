from team import Team
from strategy import Strategy

class Coach:
    def __init__(self):
        self.__team = Team("Hurstville Hornets")
        self.__strategy = Strategy()
    
    def use(self):
        while (choice := input("Choice (p/t/s/x): ")) != 'x':
            if choice == 'p':
                self.play()
            elif choice == 't':
                self.view_stats()
            elif choice == 's':
                self.view_strategy()
            else:
                self.help()
    
    def play(self):
        print(f"Playing game with a focus on {self.__strategy}")
        result = self.__team.play()

        #Ignoring draws
        if result >= 0:
            print(f"Game won by {result} points")
        else:
            print(f"Game lost by {result*-1} points")
        
        if result <= -20:
            self.__strategy.change_stratgy()

    def view_stats(self):
        print("Statistics for", self.__team)
        print("Biggest win:", self.__team.best())
        print("Biggest loss:", self.__team.worst())
        print(f"Average margin: {self.__team.average():.2f}")

    def view_strategy(self):
        print(f"Current strategy for {self.__team}: {self.__strategy}")

    def help(self):
        print("Menu options:")
        print("p = play game")
        print("t = team stats")
        print("s = current strategy")

if __name__ == "__main__":
    coach = Coach()
    coach.use()