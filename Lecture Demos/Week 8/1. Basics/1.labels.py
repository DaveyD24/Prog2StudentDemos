from tkinter import *

root = Tk()

label1 = Label(root)
label1.config(text="Welcome to the lecture", background="blue")
label1.pack()

label2 = Label(root)
label2.config(text="By David Dyer", background="red")
label2.pack()

root.mainloop()