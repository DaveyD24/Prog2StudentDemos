from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut
from GameView import GameView

class GamesView:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.tree = None

    def control(self):
        ut.Image(self.window, "../../images/rugby.png").pack()
        ut.Separator(self.window).pack(fill=X, expand=True, pady=(20,20))
        self.setup_tree()
        ut.Separator(self.window).pack(expand=True, fill=X, pady=(20,20))
        
        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "View Selected Games", self.open_games).pack(expand=True, fill=X, side=LEFT)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

    def setup_tree(self):
        self.tree = ttk.Treeview(self.window, columns=("homeTeamCol", "scoreCol", "awayTeamCol"), show="headings")
        for column in self.tree["columns"]:
            self.tree.column(column, anchor=CENTER)
        self.tree.heading("homeTeamCol", text="Home")
        self.tree.heading("scoreCol", text="Score")
        self.tree.heading("awayTeamCol", text="Away")
        for game in self.model:
            score = f"{game.home.score} - {game.away.score}"
            self.tree.insert('', END, values=(game.home.team.name, score, game.away.team.name))
        self.tree.pack()

    def game(self, home, away):
        for game in self.model.games:
            if game.home.name == home and game.away.name == away:
                return game
        return None
    
    def get_selections(self):
        selections = []
        print(self.tree.selection())
        for item in self.tree.selection():
            it = (self.tree.item(item, option="value"))
            selections.append(self.game(it[0], it[2]))
        return selections

    def game(self, home, away):
        for game in self.model:
            if game.home.team.name == home and game.away.team.name == away:
                return game
        return None

    def open_games(self):
        for game in self.get_selections():
            GameView(Toplevel(), game).control()

    def close(self):
        self.window.destroy()