from tkinter import *
from tkinter import ttk

def on_press(event):
    label.config(background="red")

def on_release(event):
    label.config(background="grey")

root = Tk()
Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

content = Frame()
content.pack()

label = Label(content, text="Key Detected", width=150, background="grey", font=20)
label.pack(fill=X)

root.bind('<KeyPress>', on_press)
root.bind('<KeyRelease>', on_release)

Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()