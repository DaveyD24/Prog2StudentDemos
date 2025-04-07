from tkinter import *
from tkinter import ttk
from Utils.Utils import Utils as ut

class TeamsView:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.tree = None
    
    def control(self):
        self.tree = ttk.Treeview(self.window, columns=("locCol", "nameCol", "winPercentCol"), show="headings")
        self.tree.heading("locCol", text="Location")
        self.tree.heading("nameCol", text="Name")
        self.tree.heading("winPercentCol", text="Win Percent")
       
        for team in self.model:
            test = self.tree.insert('', END, values=(team.location, team.name, team.win_percentage()))
        self.tree.pack()

        ut.Button(self.window, "Select", self.select).pack(side=LEFT, expand=True, fill=X)

    def select(self):
        print(self.get_selected())

    def get_selected(self):
        for team in self.model:
            if self.tree.item(self.tree.selection()[0], option="values")[0] == team.location:
                return team
        return None