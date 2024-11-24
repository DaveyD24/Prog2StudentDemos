from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut

class GameView:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.configure(bg="white")
    
    def control(self):
        frame = ut.Frame(self.window)
        frame.configure(background="white")
        ut.SquareImage(frame, self.model.home.team.image_path).pack(side=LEFT)
        ut.Label(frame, self.model.home.score).pack(side=LEFT)
        ut.Label(frame, "-").pack(side=LEFT)
        ut.Label(frame, self.model.away.score).pack(side=LEFT)
        ut.SquareImage(frame, self.model.away.team.image_path).pack(side=LEFT)
        frame.pack()

        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

        for widget in self.window.pack_slaves():
            widget.configure(background="white")
    
    def close(self):
        self.window.destroy()
