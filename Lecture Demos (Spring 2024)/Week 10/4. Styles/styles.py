#treeview with strings
#treeview with model data (just toString of the model)

from tkinter import *
from tkinter import ttk
from Utils import Utils as ut
from PIL import Image, ImageTk

class Application:
    def __init__(self, root):
        self.root = root
        self.tree = None

    def control(self):
        self.content()
    
    def content(self):
        ut.Image(self.root, "supplier.png").pack()
        ut.Separator(self.root).pack(fill=X, pady=(20, 20))
        ut.Label(self.root, "This is a heading").pack()
        ut.Separator(self.root).pack(fill=X, pady=(20, 20))

        btnFrame = ut.Frame(self.root)
        ut.Button(btnFrame, "Example", self.example).pack(fill=X, expand=True, side=LEFT)
        ut.Button(btnFrame, "Close", self.close).pack(fill=X, expand=True, side=LEFT)
        btnFrame.pack(fill=X, expand=True)

        ########How we would have to do it without Utils########
        # image_ = ImageTk.PhotoImage(Image.open("supplier.png").resize((600, 150)))
        # lbl = Label(root, image=image_)
        # lbl.photo = image_
        # lbl.pack()

        # ttk.Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=(20,20))
        # Label(self.root, text="This is a heading", font="Helvetica 12 bold", foreground="#168FC1").pack()
        # ttk.Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=(20,20))

        # btnFrame = Frame(self.root, width=600)
        # Button(btnFrame, text="Example", command=self.example, background="#168FC1", padx=0, relief=FLAT, font="Arial 11 bold", foreground="white").pack(fill=X, expand=True, side=LEFT)
        # Button(btnFrame, text="Close", command=self.close, background="#168FC1", padx=0, relief=FLAT, font="Arial 11 bold", foreground="white").pack(fill=X, expand=True, side=LEFT)
        # btnFrame.pack(fill=X, expand=True)

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