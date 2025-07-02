from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut
from GamesView import GamesView
from TeamsView import TeamsView

class SeasonView:
    def __init__(self, window, model):
        self.window = window
        self.model = model

    def control(self):
        ut.Image(self.window, "../../images/rugby.png").pack()
        ut.Separator(self.window).pack(fill=X, expand=True, pady=(20,20))
        ut.Label(self.window, "Season underway").pack()
        ut.Separator(self.window).pack(expand=True, fill=X, pady=(20,20))
        
        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "View Teams", self.view_teams).pack(expand=True, fill=X, side=LEFT)
        ut.Button(btnFrame, "View Games", self.view_games).pack(expand=True, fill=X, side=LEFT)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

    def view_teams(self):
        TeamsView(Toplevel(), self.model.teams).control()

    def view_games(self):
        GamesView(Toplevel(), self.model.games).control()
    
    def close(self):
        self.window.destroy()