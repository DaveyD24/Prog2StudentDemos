from tkinter import *
from PIL import Image, ImageTk

class TkUtils:
    class Image(Label):
        #TODO: Fix this Img thing
        def __init__(self, parent, path, width, height, background=None):
            image_ = ImageTk.PhotoImage(Image.open(path).resize((width, height)))
            super().__init__(parent, image=image_, background=background)
            self.photo = image_