from tkinter import *
from tkinter import ttk

def set_team():
    print(f"You support {lb.selection_get()}")

root = Tk()
Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

team = StringVar()
combo = ttk.Combobox(root, textvariable=team)
combo.config(values=('Broncos', 'Titans', 'Storm'))
combo.pack()

lb = Listbox(root, width=150)
lb.insert(0, "Broncos", "Titans", "Storm")
lb.pack()

button = ttk.Button(root, text="Thats my team!", command= set_team)
button.pack()

Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()