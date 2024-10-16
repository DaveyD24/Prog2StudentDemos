from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.tree = None

    def control(self):
        self.header()
        self.content()
        self.footer()
    
    def content(self):
        contentFrame = Frame(self.root)
        self.setup_tree(contentFrame)
        self.setup_buttons(contentFrame)
        contentFrame.pack()

    def setup_tree(self, frame):
        teams = ['Broncos', 'Storm', 'Titans', 'Roosters']
        self.tree = ttk.Treeview(frame)
        self.tree.heading("#0", text="Team")
        self.tree.config(selectmode="extended")
        for team in teams:
            self.tree.insert('', END, text=(team))
        self.tree.pack()

    def setup_buttons(self, frame):
        checkBtn = Button(frame, text="Check", background="blue", foreground="white", font="Arial 12 bold", relief=FLAT, command= self.check)
        checkBtn.pack(fill=X, expand=True)

    def get_selections(self):
        return [self.tree.item(id, option="text") for id in self.tree.selection()]

    def check(self):
        ids = self.tree.selection()
        items = []
        for id in ids:
            item = self.tree.item(id, option="text")
            items.append(item)
        print(items)

    def header(self):
        Label(self.root, text="Lecture 10", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n')
    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12').pack(fill=X, expand=True, anchor='s')
    
if __name__ == "__main__":
    root = Tk()
    Application(root).control()
    root.mainloop()