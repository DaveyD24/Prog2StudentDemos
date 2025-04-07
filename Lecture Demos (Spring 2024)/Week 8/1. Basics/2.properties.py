from tkinter import *

root = Tk()

header = Label(root, text="Lecture 8", background="grey", foreground="white", font="Helvetica 18 bold").pack(fill=X, anchor="n", pady=(0,10))
footer = Label(root, text="David Dyer", background="grey", foreground="white", font="Helvetica 12").pack(fill=X, anchor="s", expand=True, pady=(10, 0))

root.mainloop()