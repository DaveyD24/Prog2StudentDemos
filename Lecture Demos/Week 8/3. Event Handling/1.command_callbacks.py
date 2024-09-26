from tkinter import *
from tkinter import ttk

def order(status):
    print(f"Proceeding to {status} your order for {combo.get()}")

root = Tk()
Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

product = StringVar()
combo = ttk.Combobox(root, textvariable=product)
combo.config(values=('Banana', 'Red Bull', 'Biscuit'))
combo.pack()

button1 = Button(text = "Submit", command= lambda: order("submit"))
button2 = Button(text= "Cancel", command = lambda: order("cancel"))
button1.pack()
button2.pack()

Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()