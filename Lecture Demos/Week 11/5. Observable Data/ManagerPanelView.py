from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut 

class ManagerPanelView:
    def __init__(self, window, model, observableView):
        self.window = window
        self.model = model
        self.observableView = observableView
    
    def control(self):
        ut.Label(self.window, "Manager Panel").pack()
        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "Replay Season", self.replay_season).pack(expand=True, fill=X, side=LEFT)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack()
    
    def replay_season(self):
        self.model.play_season()
        self.observableView.update_premiers()
        self.observableView.update_games()

    def close(self):
        self.window.destroy()
