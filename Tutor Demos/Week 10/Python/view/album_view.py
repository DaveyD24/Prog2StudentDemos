from tkinter import *
from model.album import Album
from tk_utils import TkUtils
from view.style import Style

class AlbumView:
    def __init__(self, parent, model: Album):
        self.parent = parent
        self.model = model
        self.parent.title(self.model.get_name())
        self.model.subscribe(self.update_stats)
        self.model.subscribe(self.update_buttons)

        image_path = "view/image/" + self.model.get_name() + ".jpg"
        TkUtils.Image(self.parent, image_path, 200, 200).pack()

        Label(self.parent, text=self.model.get_name()).pack()
        Label(self.parent, text=self.model.get_artist()).pack()

        stats_frame = Frame(self.parent)
        Label(stats_frame, text="Units Sold:", **Style.label).pack(side=LEFT)
        self.sold_txt = Label(stats_frame, text="0")
        self.sold_txt.pack(side=LEFT)

        Label(stats_frame, text="Profit:", **Style.label).pack(side=LEFT)
        self.profit_txt = Label(stats_frame, text="0")
        self.profit_txt.pack(side=LEFT)

        stats_frame.pack(pady=10)

        self.purchase_btn = Button(self.parent, text="Purchase", command=self.purchase, **Style.button)
        self.purchase_btn.pack(**Style.pack_stretch)

    def update_stats(self):
        self.sold_txt.configure(text=self.model.get_sold())
        self.profit_txt.configure(text=f"${self.model.get_profit():.2f}")

    def update_buttons(self):
        if not self.model.can_sell():
            self.purchase_btn.configure(state=DISABLED)

    def purchase(self):
        self.model.sell()