from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut
from GamesView import GamesView
from Model.Premiership import Premiership

class PremiershipView:
    def __init__(self, window, model):
        self.window = window
        self.model = model

    def control(self):
        ut.Image(self.window, "rugby.png").pack()
        ut.Separator(self.window).pack(fill=X, expand=True, pady=(20,20))
        ut.Label(self.window, "Telstra Premiership 2024").pack()
        ut.Separator(self.window).pack(expand=True, fill=X, pady=(20,20))
        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "Begin Season", self.begin_season).pack(expand=True, fill=X, side=LEFT)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

    def begin_season(self):
        self.model.play_season()
        GamesView(ut.SameWindow(self.window), self.model).control()
    
    def close(self):
        self.window.destroy()

if __name__ == "__main__":
    root = Tk()
    PremiershipView(root, Premiership()).control()
    root.mainloop()