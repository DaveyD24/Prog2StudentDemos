from tkinter import *
from tkinter import ttk
from Utils import Utils as ut

class Application:
    def __init__(self, root):
        self.root = root
        self.tree = None
        self.entry = None
        self.hideBtn = None

    def control(self):
        self.header()
        self.content()
        self.footer()
        self.setup_bindings()
    
    def content(self):
        self.entry = ttk.Entry(self.root)
        self.entry.pack()
        self.setup_tree()

        btnFrame = Frame(self.root)
        self.hideBtn = ut.Button(btnFrame, "Hide Me", self.example)
        self.hideBtn.config(state=DISABLED)
        self.hideBtn.pack(fill=X, expand=True, side=LEFT)
        btn1 = ut.Button(btnFrame, "Close", self.close).pack(fill=X, expand=True, side=LEFT)
        btnFrame.pack()

    def get_selection(self):
        return self.tree.item(self.tree.selection()[0], option="text")

    def setup_tree(self):
        teams = ['Broncos', 'Storm', 'Titans', 'Roosters']
        self.tree = ttk.Treeview(self.root)
        self.tree.heading("#0", text="Team")
        self.tree.config(selectmode="browse")
        for team in teams:
            self.tree.insert('', END, text=(team))
        self.tree.pack()

    def setup_bindings(self):
        ######## Binding for Entry Box ########
        #self.entry.bind("<KeyRelease>", self.hide)
        ########################################

        self.tree.bind("<<TreeviewSelect>>", self.hide)

    def hide(self, event):
        
        ######## Listener for Entry Box ########
        # if self.entry.get() == None or self.entry.get() == "":
        #     self.hideBtn.config(state=DISABLED)
        # else:
        #     self.hideBtn.config(state=NORMAL)
        ########################################

        if self.get_selection() == None:
            self.hideBtn.config(state=DISABLED)
        else:
            self.hideBtn.config(state=NORMAL)

    def example(self):
        pass

    def close(self):
        self.root.destroy()

    def header(self):
        Label(self.root, text="Lecture 10", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n')
    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12').pack(fill=X, expand=True, anchor='s')
    
if __name__ == "__main__":
    root = Tk()
    Application(root).control()
    root.mainloop()