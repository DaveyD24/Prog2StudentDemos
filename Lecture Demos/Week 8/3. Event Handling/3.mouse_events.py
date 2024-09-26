from tkinter import *
from tkinter import ttk

def on_press(event):
    mice = [leftmouse, middlemouse,rightmouse]
    mice[event.num - 1].config(background="red")

def on_release(event):
    if event.num == 1:
        leftmouse.config(background="#4d4d4d")
    elif event.num == 2:
        middlemouse.config(background="#262626")
    elif event.num == 3:
        rightmouse.config(background="#4d4d4d")

root = Tk()
Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

content = Frame(root, height=500)
content.pack()

leftmouse = Label(content, width=20, height=30, background="#4d4d4d", font=50)
leftmouse.pack(fill=X, side=LEFT)
middlemouse = Label(content, width=5, height=30, background="#262626", font=50)
middlemouse.pack(fill=X, side=LEFT)
rightmouse = Label(content, width=20, height=30, background="#4d4d4d", font=50)
rightmouse.pack(fill=X, side=LEFT)

for widget in content.pack_slaves():
    widget.bind('<ButtonPress>', on_press)
    widget.bind('<ButtonRelease>', on_release)

Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()