from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import ttk

root = Tk()
header = Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold')
header.pack(fill=X, expand=True, anchor='n', pady=(0, 10))


entry = Entry(root, width=50)
entry.config(show ="*")
entry.pack(pady=(15,15))



def submit():
    print(f"You chose: {entry.get()}")

button = ttk.Button(root, text="Okay")
button.config(command= submit)
button.pack()


footer = Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()