from tkinter import *
from PIL import ImageTk, Image
from model.record_store import RecordStore

class RecordStoreView:
    def __init__(self, parent, model: RecordStore):
        self.parent = parent
        self.parent.title("Record Store")
        self.model = model

        image_ = ImageTk.PhotoImage(Image.open("view/image/Serenity.jpg").resize((250, 250)))
        lbl = Label(self.parent, image=image_)
        lbl.photo = image_
        lbl.pack()

        Label(self.parent, text=self.model.get_album().get_name()).pack()
        Label(self.parent, text=self.model.get_album().get_artist()).pack()
        
        self.purchase_btn = Button(self.parent, text="Purchase", command=self.purchase)

        stats_frame = Frame(self.parent)
        Label(stats_frame, text="Units Sold:").pack(side=LEFT)
        self.sold_txt = Label(stats_frame, text="0")
        self.sold_txt.pack(side=LEFT)

        Label(stats_frame, text="Profit:").pack(side=LEFT)
        self.profit_txt = Label(stats_frame, text="0")
        self.profit_txt.pack(side=LEFT)

        stats_frame.pack(pady=10)

        self.purchase_btn.pack(fill=X, expand=TRUE)

    def purchase(self):
        self.model.get_album().sell()
        self.sold_txt.configure(text=self.model.get_album().get_sold())
        self.profit_txt.configure(text=f"${self.model.get_album().get_profit():.2f}")

        if not self.model.get_album().can_sell():
            self.purchase_btn.configure(state=DISABLED)