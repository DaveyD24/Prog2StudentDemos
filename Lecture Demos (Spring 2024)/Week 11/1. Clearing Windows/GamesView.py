from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut

class GamesView:
    def __init__(self, window, model):
        self.window = window
        self.clear_window()
        self.model = model

    def clear_window(self):
        for widget in self.window.pack_slaves():
            widget.destroy()

    def control(self):
        ut.Image(self.window, "../../images/rugby.png").pack()
        ut.Separator(self.window).pack(fill=X, expand=True, pady=(20,20))
        for game in self.model.games:
            ut.Label(self.window, game).pack()
        ut.Separator(self.window).pack(expand=True, fill=X, pady=(20,20))
        
        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

    def close(self):
        self.window.destroy()