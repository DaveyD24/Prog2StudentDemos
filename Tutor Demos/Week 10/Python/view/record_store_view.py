from tkinter import *
from tkinter import ttk
from model.record_store import RecordStore
from tk_utils import TkUtils
from view.style import Style
from view.album_view import AlbumView

class RecordStoreView:
    def __init__(self, parent, model: RecordStore):
        self.parent = parent
        self.model = model
        self.parent.title("Record Store")
        self.model.subscribe(self.update_list)

        TkUtils.Image(self.parent, "view/image/banner.jpg", 540, 300).pack()

        ttk.Separator(self.parent, orient=HORIZONTAL).pack(**Style.pack_stretch, pady=10)
        Label(self.parent, text="Albums").pack(**Style.pack_stretch)
        ttk.Separator(self.parent, orient=HORIZONTAL).pack(**Style.pack_stretch, pady=10)

        self.lb = Listbox(self.parent, height=10, width=50)
        for album in self.model.get_albums():
            self.lb.insert(END, str(album))
        self.lb.pack(pady=5, **Style.pack_stretch)

        btn_frame = Frame()
        self.view_btn = Button(self.parent, **Style.button, text="View", command=self.view, state=DISABLED)
        self.view_btn.pack(**Style.pack_stretch, side=LEFT)
        self.remove_btn = Button(self.parent, **Style.button, text="Remove", command=self.remove, state=DISABLED)
        self.remove_btn.pack(**Style.pack_stretch, side=LEFT)
        Button(self.parent, **Style.button, text="Close", command=self.close).pack(**Style.pack_stretch, side=LEFT)
        btn_frame.pack(**Style.pack_stretch)

        self.lb.bind("<<ListboxSelect>>", self.update_buttons)

    def update_list(self):
        self.lb.delete(0, END)
        for album in self.model.get_albums():
            self.lb.insert(END, str(album))

    def update_buttons(self, event):
        self.view_btn.configure(state= DISABLED if self.get_selected_album() == None else NORMAL)
        self.remove_btn.configure(state= DISABLED if self.get_selected_album() == None else NORMAL)

    def get_selected_album(self):
        if len(self.lb.curselection()) == 0:
            return None
        idx = self.lb.curselection()[0]
        return self.model.get_albums()[idx]

    def view(self):
        AlbumView(Toplevel(self.parent), self.get_selected_album())

    def remove(self):
        self.model.remove(self.get_selected_album())

    def close(self):
        self.parent.destroy()