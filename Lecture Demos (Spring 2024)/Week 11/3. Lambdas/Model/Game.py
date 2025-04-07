import random

class Game:
    def __init__(self, home_team, away_team):
        self.home = MatchCard(home_team, 0)
        self.away = MatchCard(away_team, 0)
    
    def play(self):
        self.home.score = random.randint(10,99)
        self.away.score = random.randint(0,89)
        self.winner().team.wins += 1
        self.loser().team.losses += 1

    def winner(self):
        return self.home if self.home.score > self.away.score else self.away

    def loser(self):
        return self.home if self.home.score < self.away.score else self.away

    def __str__(self):
        return f"{self.winner().team} {self.winner().score} - {self.loser().score} {self.loser().team}"

class MatchCard:
    def __init__(self, team, score):
        self.team = team
        self.score = score
    