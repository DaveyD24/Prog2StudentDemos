from tkinter import *
from PIL import ImageTk, Image
from record_store import RecordStore

class RecordStoreView:
    def __init__(self, root, model):
        self.root = root
        self.root.title("Record Store")
        self.model = model

        self.sold_txt = None
        self.profit_txt = None
        self.purchase_btn = None

    def control(self):

        image_ = ImageTk.PhotoImage(Image.open("image/Serenity.jpg").resize((250, 250)))
        lbl = Label(self.root, image=image_)
        lbl.photo = image_
        lbl.pack()
        album_txt = Label(self.root, text=self.model.album.name)
        artist_txt = Label(self.root, text=self.model.album.artist)
        self.purchase_btn = Button(self.root, text="Purchase", command=self.purchase)

        album_txt.pack()
        artist_txt.pack()

        stats_frame = Frame(self.root)
        sold_lbl = Label(stats_frame, text="Units Sold:")
        self.sold_txt = Label(stats_frame, text="0")
        profit_lbl = Label(stats_frame, text="Profit:")
        self.profit_txt = Label(stats_frame, text="0")
        sold_lbl.pack(side=LEFT)
        self.sold_txt.pack(side=LEFT)
        profit_lbl.pack(side=LEFT)
        self.profit_txt.pack(side=LEFT)
        stats_frame.pack(pady=(10,10))

        self.purchase_btn.pack(fill=X, expand=TRUE)

    def purchase(self):
        if self.model.album.stock > 0:
            self.model.album.sell()
        self.sold_txt.config(text=str(self.model.album.sold))
        self.profit_txt.config(text=f"${self.model.album.profit:.2f}")
        if self.model.album.stock == 0:
            self.purchase_btn.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    RecordStoreView(root, RecordStore()).control()
    root.mainloop()