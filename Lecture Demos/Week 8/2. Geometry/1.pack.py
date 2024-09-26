from tkinter import *
from tkinter import ttk

root = Tk()
Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

content = Frame(root)
content.pack()

label1 = Label(content, text="Item 1", background="blue", font=15).pack(side=LEFT)
label2 = Label(content, text="Item 2", background="red", font=15).pack(side=LEFT)
label3 = Label(content, text="Item 3", background="green", font=15).pack(side=LEFT)

Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()