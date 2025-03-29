from tkinter import *

root = Tk()

def plus():
    intVar.set(intVar.get() + 1)

def minus():
    intVar.set(intVar.get() - 1)

def clear():
    intVar.set(0)

valueLbl = Label(root, text="Value: ")
intVar = IntVar()
valueEntry = Entry(root, textvariable=intVar)
plusBtn = Button(root, text="+", command=plus)
minusBtn = Button(root, text="-", command=minus)
clearBtn = Button(root, text="C", command=clear)

valueLbl.pack(side=LEFT)
valueEntry.pack(side=LEFT)
plusBtn.pack(side=LEFT)
minusBtn.pack(side=LEFT)
clearBtn.pack(side=LEFT)

root.title("Incrementer")
root.mainloop()
