from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Application:
    def __init__(self, root):
        self.root = root
        self.setup_scene()
        self.header()
        self.content()
        self.footer()

    def disable(self):
        pass

    def setup_scene(self):
        self.root.title('Lecture 9')
        self.root.resizable(False, False)
        img = ImageTk.PhotoImage(Image.open('cat_icon.png'))
        self.root.iconphoto(False, img)
        self.root.protocol("WM_DELETE_WINDOW", self.disable)

    def header(self):
        Label(self.root, text="Lecture 9", background="grey", foreground="white", font='Helvetica 18 bold').pack(fill=X, expand=True, anchor='n')

    def content(self):
        self.setup_picture()
        self.setup_content()
        self.setup_buttons()

    def footer(self):
        Label(self.root, text="David Dyer", background="grey", foreground="white", font='Helvetica 12').pack(fill=X, expand=True, anchor='s')

    def setup_picture(self):
        frame = Frame(self.root)
        header_image = ImageTk.PhotoImage(Image.open('cat.jpg').resize((300, 300)))
        lbl = Label(frame, image=header_image)
        lbl.photo = header_image
        lbl.pack()
        frame.pack(padx=(0,0))

    def setup_content(self):
        self.seperator()
        frame = Frame(self.root)
        Label(frame, text="This should help with the assignment", foreground="blue", font="Arial 12 bold").pack()
        frame.pack()
        self.seperator()

    def setup_buttons(self):
        frame = Frame(self.root)
        Button(frame, text="Button 1", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold").pack(side=LEFT, fill=X, expand=True)
        Button(frame, text="Close", foreground="white", background="blue", relief=FLAT, font="Arial 10 bold", command=self.close).pack(side=LEFT, fill=X, expand=True)
        frame.pack(expand=True, fill=X)

    def close(self):
        self.root.destroy()

    def seperator(self):
        ttk.Separator(root).pack(fill=X, pady=(10, 10))


if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()