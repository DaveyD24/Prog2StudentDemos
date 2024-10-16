from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root

    def control(self):
        self.header()
        self.content()
        self.footer()
    
    def content(self):
        teams = ['Broncos', 'Storm', 'Titans', 'Roosters']
        tree = ttk.Treeview(self.root)
        tree.config(selectmode="none")
        tree.heading("#0", text="Team")
        for team in teams:
            tree.insert('', END, text=(team))
        tree.pack()

    def header(self):
        Label(self.root, text="Lecture 10", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n')
    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12').pack(fill=X, expand=True, anchor='s')
    
if __name__ == "__main__":
    root = Tk()
    Application(root).control()
    root.mainloop()