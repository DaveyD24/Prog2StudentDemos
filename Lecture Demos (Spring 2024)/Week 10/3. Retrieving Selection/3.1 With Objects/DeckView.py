from tkinter import *
from tkinter import ttk
from Deck import Deck
from CardView import CardView

class DeckView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.tree = None

    def control(self):
        self.header()
        self.content()
        self.footer()
    
    def content(self):
        contentFrame = Frame(self.root)
        self.setup_tree(contentFrame)
        self.setup_buttons(contentFrame)
        contentFrame.pack()

    def setup_tree(self, frame):
        self.tree = ttk.Treeview(frame, height=13)
        self.tree.heading("#0", text="Card")
        self.tree.config(selectmode="browse")
        for card in self.model.cards:
            self.tree.insert('', END, text=(card.__str__()))
        self.tree.pack()

    def setup_buttons(self, frame):
        checkBtn = Button(frame, text="Preview Card", background="blue", foreground="white", font="Arial 12 bold", relief=FLAT, command= self.open_card)
        checkBtn.pack(fill=X, expand=True)

    def card(self, card_string):
        for card in self.model.cards:
            if card.__str__() == card_string:
                return card

    def get_selection(self):
        item_string = self.tree.item(self.tree.selection()[0], option="text")
        card = self.card(item_string)
        return card

    def open_card(self):
        CardView(Toplevel(), self.get_selection()).control()

    def header(self):
        Label(self.root, text="Lecture 10", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n')
    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12').pack(fill=X, expand=True, anchor='s')
    
if __name__ == "__main__":
    root = Tk()
    DeckView(root, Deck()).control()
    root.mainloop()