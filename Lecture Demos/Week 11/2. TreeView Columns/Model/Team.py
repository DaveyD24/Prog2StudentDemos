class Team:
    def __init__(self, location, name):
        self.location = location
        self.name = name
        self.wins = 0
        self.losses = 0
        self.drawn = 0
    
    def win_percentage(self):
        games_played = self.wins + self.drawn + self.losses
        return 0 if games_played == 0 else self.wins/(games_played)*100

    def __str__(self):
        return f"{self.location} {self.name} (Win Percent: {self.win_percentage():.0f}%)"

    def values(self):
        print(f"Wins: {self.wins}, Losses: {self.losses}, Drawn: {self.drawn}")