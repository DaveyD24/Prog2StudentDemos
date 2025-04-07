from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Dealer import Dealer
from DeckView import DeckView

class DealerView:
    def __init__(self, window, model):
        self.window = window
        self.model = model

    def control(self):
        self.setup_content()
        self.setup_buttons()

    def setup_content(self):
        dealer_name = self.model.__str__()
        Label(self.window, text=f"Welcome {dealer_name}", font="Helvetica 18 bold").pack()

    def setup_buttons(self):
        frame = Frame(self.window)
        Button(frame, text="View Deck", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold", command=self.deck).pack(side=LEFT, fill=X, expand=True)
        Button(frame, text="Close", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold", command=self.close).pack(side=LEFT, fill=X, expand=True)
        frame.pack(expand=True, fill=X)

    def deck(self):
        DeckView(Toplevel(), self.model.deck).control()

    def close(self):
        self.window.destroy()


if __name__ == "__main__":
    root = Tk()
    DealerView(root, Dealer()).control()
    root.mainloop()