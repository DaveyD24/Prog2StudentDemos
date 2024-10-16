from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root

        top_frame = Frame(root, width=300)
        Label(top_frame, text="Enter text: ").pack(side=LEFT)
        Entry(top_frame, text="Enter text: ").pack(side=LEFT)
        Button(top_frame, text="Submit").pack(side=LEFT)
        top_frame.pack()

        ttk.Separator(root).pack(fill=X, pady=(10, 10))

        bottom_frame = Frame(root, width=300)
        ttk.Label(bottom_frame, text="Enter text: ").pack(side=LEFT)
        ttk.Entry(bottom_frame, text="Enter text: ").pack(side=LEFT)
        ttk.Button(bottom_frame, text="Submit").pack(side=LEFT)
        bottom_frame.pack()

if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()