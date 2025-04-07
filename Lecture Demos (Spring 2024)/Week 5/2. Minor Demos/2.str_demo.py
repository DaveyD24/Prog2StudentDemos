class Team:
    def __init__(self, location, team_name, wins, losses) -> None:
        self.location = location
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
    
    def win_percentage(self) -> float:
        return (self.wins / (self.wins + self.losses)) * 100

    def __str__(self) -> str:
        return f"{self.location} {self.team_name} ({self.win_percentage()}% Win Rate)"

if __name__ == "__main__":
    storm = Team("Melbourne", "Storm", 18, 6)
    print(storm)
    print(storm.__repr__())