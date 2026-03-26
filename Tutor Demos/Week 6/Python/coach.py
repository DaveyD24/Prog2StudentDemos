from team import Team
from strategy import Strategy

class Coach:
    def __init__(self):
        self.__team = Team("Hurstville Hornets")
        self.__teams = []
        self.__teams.extend([Team("Broadway Bulldogs"), Team("Olympic Leopards"), Team("Chippendale Panthers"), Team("West-Broadway Lions"), Team("Engadine Sea-Lions"),])
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

    def matches(self, substring):
        matches = []
        for t in self.__teams:
            if t.has(substring):
                matches.append(t)
        return matches

    def play(self):
        sub = input("Enter the team to play against:")
        matches = self.matches(sub)

        if len(matches) == 0:
            print("No such team in the league")
        else:
            for opponent in matches:
                self.play_game(opponent)


    def play_game(self, opponent):
        print(f"Playing game against {opponent} with a focus on {self.__strategy}")
        result = self.__team.play(opponent)

        #Ignoring draws
        if result >= 0:
            print(f"Game won by {result} points")
        else:
            print(f"Game lost by {result*-1} points")
        
        if result <= -20:
            self.__strategy.change_strategy()

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