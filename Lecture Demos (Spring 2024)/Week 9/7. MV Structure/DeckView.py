from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Dealer import Dealer
from CardView import CardView

class DeckView:
    def __init__(self, window, model):
        self.window = window
        self.model = model

    def control(self):
        self.setup_content()
        self.setup_buttons()

    def setup_content(self):
        Label(self.window, text=f"Size of deck: {len(self.model.cards)}".__str__()).pack()

    def setup_buttons(self):
        frame = Frame(self.window)
        Button(frame, text="View Card", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold", command=self.card).pack(side=LEFT, fill=X, expand=True)
        Button(frame, text="Close", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold", command=self.close).pack(side=LEFT, fill=X, expand=True)
        frame.pack(expand=True, fill=X)

    def card(self):
        print(self.model.get_random())
        # for card in self.model.cards:
        #     CardView(Toplevel(), card).control()
        CardView(Toplevel(), self.model.get_random()).control()

    def close(self):
        self.window.destroy()