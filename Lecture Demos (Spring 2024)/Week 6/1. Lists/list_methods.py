class Team:
    def __init__(self, location, name, wins, losses):
        self.location = location
        self.name = name
        self.wins = wins
        self.losses = losses
    
    def win_percentage(self) -> int:
        return (self.wins / (self.wins + self.losses) * 100)

    def __repr__(self) -> str:
        return f"{self.location} {self.name} ({self.win_percentage():.2f}% Win Rate)"

if __name__ == "__main__":
    teams = [Team("Melbourne", "Storm", 18, 6), Team("Brisbane", "Broncos", 10, 12)]
    
    #Uncomment the lines below and observe that line 19 appears to append to both lists. teams2 is a reference to the same memory that teams is pointing to
    # teams2 = teams
    # teams2.append(Team("Gold Coast", "Titans", 0, 24))
    # print(teams)
    # print(teams2)
    
    teams_copy = teams.copy()
    teams_copy.append(Team("Gold Coast", "Titans", 0, 24))
    print(teams)
    print(teams_copy)