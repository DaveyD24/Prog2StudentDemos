from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

#You will never have to manually call this, It's used as part of one of the static methods
class ObservableButton(Button):
    def __init__(self, root, text, callback, main_color, hover_color):
        Button.__init__(self, root, text=text, command=callback, background=main_color, padx=0, relief=FLAT,
                   font="Arial 11 bold", foreground="white")
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_exit)
        self.main_color = main_color
        self.hover_color = hover_color

    def on_hover(self, event):
        self["background"] = self.hover_color

    def on_exit(self, event):
        self["background"] = self.main_color

class TkUtils:
    red = "#ff8f8f"

    @staticmethod
    def root():
        window = Tk()
        window.configure(background="#f4f4f4")
        return window

    @staticmethod
    def top_level(title_, height=0):
        tl = Toplevel()
        tl.resizable(False, False)
        tl.title(title_)
        tl.configure(background="#f4f4f4")
        return tl

    @staticmethod
    def button(root, text_, callback=None):
        return ObservableButton(root, text_, callback, TkUtils.red, "#ff8080")

    @staticmethod
    def separator(root):
        return ttk.Separator(root, orient='horizontal')

    @staticmethod
    def label(root, text_):
        return Label(root, text=text_, font="Helvetica 12 bold", foreground=TkUtils.red, background="#f4f4f4")

    @staticmethod
    def image(root, path, height, width, background=None):
        image_ = ImageTk.PhotoImage(Image.open(path).resize((width, height)))
        lbl = Label(root, image=image_)
        lbl.photo = image_
        if background:
            lbl.configure(background=background)
        return lbl

    #You will never have to manually call this, It's used as part of one of the static methods
    @staticmethod
    def _select(event, tree):
        item_id = tree.identify_row(event.y)
        if item_id is None:
            return
        if item_id in tree.selection():
            tree.selection_remove(item_id)
            return 'break'

    @staticmethod
    def treeview(root, columns, multi=False, width=500):
        tree = ttk.Treeview(root, show="headings", height=12, columns=columns, selectmode="extended" if multi else "browse")
        for column in tree["columns"]:
            tree.column(column, anchor=CENTER, width=int(width/len(columns)), stretch=NO)
        for i in range(len(columns)):
            tree.heading(i, text=columns[i])
        tree.bind("<<TreeViewSelect>>", 'break')
        tree.bind("<Button-1>", lambda event: TkUtils._select(event, tree))
        return tree