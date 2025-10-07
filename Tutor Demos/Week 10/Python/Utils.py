from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Utils:
    python_blue = "#be8fff"
    width = 540
    image_height = 300

    @staticmethod
    def disable():
        pass

    @staticmethod
    def root():
        window = Tk()
        window.resizable(False, False)
        window.title("Login")
        return window


    #Some operating systems struggle to automatically stretch the window
    #If needed, pass in a manual height and uncomment line 31
    @staticmethod
    def top_level(title_, height=0):
        tl = Toplevel()
        tl.resizable(False, False)
        tl.title(title_)
        # tl.geometry(f"{Utils.width}x{height}")
        return tl

    @staticmethod
    def button(root, text_, callback=None):
        return Button(root, text=text_, command=callback, background=Utils.python_blue, padx=0, relief=FLAT,
                      font="Arial 11 bold", foreground="white")
    @staticmethod
    def frame(root):
        return Frame(root, width=Utils.width)

    @staticmethod
    def separator(root):
        return ttk.Separator(root, orient='horizontal')

    @staticmethod
    def label(root, text_):
        return Label(root, text=text_, font="Helvetica 12 bold", foreground=Utils.python_blue)

    @staticmethod
    # Don't use this for the icon image
    def image(root, path, height_=image_height, width_=width):
        image_ = ImageTk.PhotoImage(Image.open(path).resize((width_, height_)))
        lbl = Label(root, image=image_)
        lbl.photo = image_
        return lbl

    @staticmethod
    def treeview(root, columns, multi=False):
        tree = ttk.Treeview(root, show="headings", height=12, columns=columns, selectmode="extended" if multi else "browse")
        for column in tree["columns"]:
            tree.column(column, anchor=CENTER, width=int(Utils.width/len(columns)), stretch=NO)
        for i in range(len(columns)):
            tree.heading(i, text=columns[i])
        tree.bind("<Motion>", 'break')
        return tree