from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.header()
        self.content()
        self.footer()

    def header(self):
        Label(self.root, text="Lecture 9", background="grey", foreground="white", font='Helvetica 18 bold', width=50).pack(fill=X, expand=True, anchor='n', pady=(0, 10))

    def content(self):
        self.setup_top()
        self.seperator()
        self.setup_bottom()

    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12', width=50).pack(fill=X, expand=True, anchor='s', pady=(10, 0))

    def setup_top(self):
        top_frame = Frame(root, width=300)
        Label(top_frame, text="Enter text: ").pack(side=LEFT)
        Entry(top_frame, text="Enter text: ").pack(side=LEFT)
        Button(top_frame, text="Submit").pack(side=LEFT)
        top_frame.pack()

    def seperator(self):
        ttk.Separator(root).pack(fill=X, pady=(10, 10))

    def setup_bottom(self):
        bottom_frame = Frame(root, width=300)
        ttk.Label(bottom_frame, text="Enter text: ").pack(side=LEFT)
        ttk.Entry(bottom_frame, text="Enter text: ").pack(side=LEFT)
        ttk.Button(bottom_frame, text="Submit").pack(side=LEFT)
        bottom_frame.pack()

if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()