from tkinter import *
from model.record_store import RecordStore
from model.album import Album
from album_view import AlbumView
from tk_utils import TkUtils as ut

class RecordStoreView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.tree = None

        self.remove_btn = None
        self.view_btn = None

    def control(self):

        ut.image(self.root, "image/banner.jpg", 300, 540).pack()
        ut.separator(self.root).pack(expand=True, fill=X, pady=(20, 20))
        ut.label(self.root, "Albums").pack()
        ut.separator(self.root).pack(expand=True, fill=X, pady=(20,20))

        self.tree = ut.treeview(self.root, columns=["Name", "Artist", "Stock", "Price"], multi=True)
        for album in self.model.albums:
            self.tree.insert('', END, values=[album.name, album.artist, album.stock, album.price])

        button_frame = Frame(self.root)
        self.remove_btn = ut.button(button_frame, "Remove", self.remove)
        self.view_btn = ut.button(button_frame, "View", self.view)
        self.remove_btn.pack(side=LEFT, fill=X, expand=True)
        self.view_btn.pack(side=LEFT, fill=X, expand=True)
        ut.button(button_frame, "Close", self.close).pack(side=LEFT, fill=X, expand=True)

        self.tree.pack()
        button_frame.pack(fill=X, expand=True)

        self.set_button_state()
        self.set_bindings()

    def set_button_state(self, event=None):
        if self.get_selected_items() is None:
            self.remove_btn.config(state=DISABLED)
            self.view_btn.config(state=DISABLED)
        else:
            self.remove_btn.config(state=NORMAL)
            self.view_btn.config(state=NORMAL)

    def set_bindings(self):
        self.tree.bind("<<TreeviewSelect>>", self.set_button_state)

    def get_selected_items(self):
        if len(self.tree.selection()) == 0:
            return None
        return [self.tree.item(x, option="values")[0] for x in self.tree.selection()]

    #Lookup pattern
    def album(self, str):
        for album in self.model.albums:
            if str == album.name:
                return album
        return None

    def remove(self):
        selected_items = self.get_selected_items()
        for item in selected_items:
            self.model.albums.remove(self.album(item))
            self.refresh()
        self.set_button_state()

    def view(self):
        selected_items = self.get_selected_items()
        for item in selected_items:
            chosen_album = self.album(item)
            AlbumView(ut.top_level(chosen_album.name), chosen_album, self).control()

    def close(self):
        self.root.destroy()

    def refresh(self):
        for node in self.tree.get_children():
            self.tree.delete(node)
        for album in self.model.albums:
            self.tree.insert('', END, values=[album.name, album.artist, album.stock, album.price])

def seeded_record_store():
    return RecordStore(albums=[
        Album("Stardust", "Serenity", 12, 34.99),
        Album("Takio Senzu", "Oceans", 12, 34.99),
        Album("Haru Yelin", "Alive", 12, 29.99),
        Album("Stardust", "Chords", 12, 29.99),
        Album("Rin Kadoshi", "Lost", 12, 29.99),
        Album("Haru Yelin", "Wind", 12, 29.99)
    ])

if __name__ == "__main__":
    root = ut.root()
    root.title("Record Store")
    RecordStoreView(root, seeded_record_store()).control()
    root.mainloop()