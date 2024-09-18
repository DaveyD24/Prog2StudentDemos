class Team:
    def __init__(self, location, name, wins, losses):
        self.location = location
        self.name = name
        self.wins = wins
        self.losses = losses
    
    def win_percentage(self) -> int:
        return (self.wins / (self.wins + self.losses) * 100)

    def __str__(self) -> str:
        return f"{self.location} {self.name} ({self.win_percentage():.2f}% Win Rate)"

if __name__ == "__main__":
    teams = [Team("Melbourne", "Storm", 18, 6), Team("Brisbane", "Broncos", 10, 12)]
    #When index isn't required
    for team in teams:
        print(team)
    
    #When index is required
    for i in range(len(teams)):
        print(f"{i+1}. {teams[i]}")

    teams_copy = teams.copy()
    teams_copy.append(Team("Gold Coast", "Titans", 0, 24))
    for team in teams_copy:
        print(team)
    print("------------")
    for team in teams:
        print(team)