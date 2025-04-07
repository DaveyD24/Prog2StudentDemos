from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut
from Model.Premiership import Premiership
from ManagerPanelView import ManagerPanelView

class PremiershipView:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.premierLbl = None
        self.model.play_season()
        self.treeFrame = None
        
    def control(self):
        ut.Image(self.window, "rugby.png").pack()
        ut.Separator(self.window).pack(fill=X, expand=True, pady=(20,20))
        self.premierLbl = ut.Label(self.window, f"Premiers: {self.model.premiers().name}")
        self.premierLbl.pack()
        ut.Separator(self.window).pack(expand=True, fill=X, pady=(20,20))

        self.treeFrame = ut.Frame(self.window)
        self.setup_tree()
        self.treeFrame.pack()


        btnFrame = ut.Frame(self.window)
        ut.Button(btnFrame, "Manager Panel", self.manager_panel).pack(expand=True, fill=X, side=LEFT)
        ut.Button(btnFrame, "Close", self.close).pack(expand=True, fill=X, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

    def setup_tree(self):
        self.tree = ttk.Treeview(self.treeFrame, columns=("homeTeamCol", "scoreCol", "awayTeamCol"), show="headings")
        for column in self.tree["columns"]:
            self.tree.column(column, anchor=CENTER)
        self.tree.heading("homeTeamCol", text="Home")
        self.tree.heading("scoreCol", text="Score")
        self.tree.heading("awayTeamCol", text="Away")
        for game in self.model.games:
            score = f"{game.home.score} - {game.away.score}"
            self.tree.insert('', END, values=(game.home.team.name, score, game.away.team.name))
        self.tree.pack()

    def manager_panel(self):
        ManagerPanelView(Toplevel(), self.model, self).control()
    
    def update_premiers(self):
        self.premierLbl.config(text=f"Premiers: {self.model.premiers().name}")
    
    def update_games(self):
        self.tree.pack_forget()
        self.setup_tree()

    def close(self):
        self.window.destroy()

if __name__ == "__main__":
    root = Tk()
    PremiershipView(root, Premiership()).control()
    root.mainloop()