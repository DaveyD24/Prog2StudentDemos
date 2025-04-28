from tkinter import *
from PIL import ImageTk, Image
from Utils import Utils as ut

class AlbumView:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.sold_txt = None
        self.profit_txt = None
        self.purchase_btn = None

    def control(self):
        image_ = ut.image(self.root, self.model.image_url, 300, 300)
        image_.pack()

        album_txt = ut.label(self.root, self.model.name)
        artist_txt = ut.label(self.root, self.model.artist)
        album_txt.pack(pady=(10, 0))
        artist_txt.pack(pady=(10, 10))

        stats_frame = ut.frame(self.root)
        sold_lbl = ut.label(stats_frame, "Units Sold:")
        self.sold_txt = ut.label(stats_frame, text_=f"{str(self.model.sold)}")
        profit_lbl = ut.label(stats_frame, "Profit:")
        self.profit_txt = ut.label(stats_frame, str(self.model.profit))
        sold_lbl.pack(side=LEFT)
        self.sold_txt.pack(side=LEFT)
        profit_lbl.pack(side=LEFT)
        self.profit_txt.pack(side=LEFT)
        stats_frame.pack()

        button_frame = Frame(self.root)
        self.purchase_btn = ut.button(button_frame, "Purchase", self.purchase)
        close_btn = ut.button(button_frame, "Close", self.close)
        self.purchase_btn.pack(side=LEFT, fill=X, expand=True)
        close_btn.pack(side=LEFT, fill=X, expand=True)
        button_frame.pack(fill=X, expand=True, pady=(10, 0))

        if self.model.stock <= 0:
            self.purchase_btn.config(state=DISABLED)

    def purchase(self):
        if self.model.stock > 0:
            self.model.sell()
        self.sold_txt.config(text=f"{self.model.sold}")
        self.profit_txt.config(text=f"{self.model.profit}")
        if self.model.stock == 0:
            self.purchase_btn.config(state=DISABLED)

    def close(self):
        self.root.destroy()
