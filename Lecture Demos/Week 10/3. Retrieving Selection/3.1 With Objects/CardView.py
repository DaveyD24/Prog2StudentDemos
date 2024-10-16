from tkinter import *
from tkinter import ttk

class CardView:
    def __init__(self, root, model):
        self.root = root
        self.model = model

    def control(self):
        self.header()
        self.content()
        self.footer()
    
    def content(self):
        Label(self.root, text=self.model.number, font="Arial 18 bold").pack()
        Label(self.root, text=self.model.suit, font="Arial 18 bold").pack()

    def header(self):
        Label(self.root, text="Lecture 10", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n')
    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12').pack(fill=X, expand=True, anchor='s')