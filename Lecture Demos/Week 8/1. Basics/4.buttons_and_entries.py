from tkinter import *
from tkinter import ttk

def submit():
    header.config(text="Watch this change")
    print(f"You typed: {entry.get()}")

root = Tk()
header = Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold')
header.pack(fill=X, expand=True, anchor='n', pady=(0, 10))

button = Button(root, text="Submit")
button.config(command= submit)
button.pack()

footer = Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()