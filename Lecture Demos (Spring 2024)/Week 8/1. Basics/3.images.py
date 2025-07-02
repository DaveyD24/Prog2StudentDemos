from tkinter import *
from PIL import ImageTk, Image

root = Tk()
header = Label(root, text="Lecture 8", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

cat = ImageTk.PhotoImage(Image.open('../../images/cat.jpg').resize((500, 500)))

label1 = Label(root, image=cat)
label1.pack()

footer = Label(root, text="David Dyer", background="grey", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()