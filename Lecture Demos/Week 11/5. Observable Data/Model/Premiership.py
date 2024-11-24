from Model.Team import Team
from Model.Game import Game

class Premiership:
    def __init__(self):
        self.teams = [Team('Brisbane', 'Broncos'), Team('Melbourne', 'Storm'), Team('Sydney', 'Roosters'), Team('Gold Coast', 'Titans')]
        self.games = []
    
    def play_season(self):
        self.teams = [Team('Brisbane', 'Broncos'), Team('Melbourne', 'Storm'), Team('Sydney', 'Roosters'), Team('Gold Coast', 'Titans')]
        self.games = []
        for team in self.teams:
            for opponent in self.teams:
                if team is not opponent:
                    game = Game(team, opponent)
                    self.games.append(game)
                    game.play()

    def premiers(self):
        return sorted(self.teams, key= lambda team : team.wins, reverse=True)[0]

if __name__ == "__main__":
    premiership = Premiership()
    premiership.play_season()