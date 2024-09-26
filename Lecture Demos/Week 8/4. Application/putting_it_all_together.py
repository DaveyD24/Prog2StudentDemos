# Specification
# Users have the option of 'Red Bull', 'Monster Energy' and 'V Blue' inside the combobox
# Users can also provide an amount in an entry box
# If both fields contain content, then the sell button should add a label underneath with the order details
# Clicking the entry field should reset the text to empty
# Cancel will exit the application

#Red Bull Colours:
#CB2026 # Red
#223971 # Blue
#FFC906 # Yellow

from tkinter import *
from tkinter import ttk

def sell():
    if entry.get() != "" and combo.get() != "":
        order = f"Bought {entry.get()} {combo.get()}"
        Label(sales, text=order, background="#FFC906", font="Helvetica 16 bold").pack(fill=X)
    
def cancel():
    root.destroy()

def reset(event):
    entry.delete(0, END)

root = Tk()
Label(root, text="Davey's Energy Drink Emporium", background="#223971", foreground="#CB2026", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n', pady=(0, 10))

options_grid = Frame(root)

product = StringVar()
combo = ttk.Combobox(options_grid, textvariable=product, width=80)
combo.config(values=['Red Bull', 'Monster Energy', 'V Blue'])
combo.pack(pady=(0, 10), side=LEFT)

entry = Entry(options_grid, width=50)
entry.pack(pady=(0, 10), padx=(5, 0), side=LEFT)
entry.bind('<1>', reset)

options_grid.pack()

buttons_grid = Frame(root)
Button(buttons_grid, text="Sell", background="red", width=50, command= sell).pack(side=LEFT)
Button(buttons_grid, text="Cancel", background="grey", width=50, command= cancel).pack(side=LEFT)
buttons_grid.pack(pady=(0, 20))

sales = Frame(root)
sales.pack(fill=X)

Label(root, text="Thanks for shopping", background="#223971", foreground="#CB2026", font='Helvetica 12').pack(fill=X, expand=True, anchor='s', pady=(10, 0))
root.mainloop()