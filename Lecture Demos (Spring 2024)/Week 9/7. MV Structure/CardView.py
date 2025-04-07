from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class CardView:
    def __init__(self, window, model):
        self.window = window
        self.model = model

    def control(self):
        self.setup_content()
        self.setup_buttons()

    def setup_content(self):
        Label(self.window, text=self.model.__str__(), font="Helvetica 18 bold").pack()

    def setup_buttons(self):
        frame = Frame(self.window)
        Button(frame, text="Close", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold", command=self.close).pack(side=LEFT, fill=X, expand=True)
        frame.pack(expand=True, fill=X)

    def close(self):
        self.window.destroy()