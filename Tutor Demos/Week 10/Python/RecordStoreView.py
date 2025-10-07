from tkinter import *
from model.RecordStore import RecordStore
from model.Albums import Albums
from model.Album import Album
from AlbumView import AlbumView
from Utils import Utils as ut

class RecordStoreView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.tree = None

        self.remove_btn = None
        self.view_btn = None

    def control(self):

        ut.image(self.root, "image/banner.png", 300, 540).pack()
        ut.separator(self.root).pack(expand=True, fill=X, pady=(20, 20))
        ut.label(self.root, "Albums").pack()
        ut.separator(self.root).pack(expand=True, fill=X, pady=(20,20))

        self.tree = ut.treeview(self.root, columns=["Albums"])
        print(self.model.albums.albums)
        for album in self.model.albums.albums:
            self.tree.insert('', END, values=[album.__str__()])

        button_frame = ut.frame(self.root)
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
        if self.get_selected_item() is None:
            self.remove_btn.config(state=DISABLED)
            self.view_btn.config(state=DISABLED)
        else:
            self.remove_btn.config(state=NORMAL)
            self.view_btn.config(state=NORMAL)

    def set_bindings(self):
        self.tree.bind("<<TreeviewSelect>>", self.set_button_state)

    def get_selected_item(self):
        if len(self.tree.selection()) == 0:
            return None
        return self.tree.item(self.tree.selection()[0], option="values")[0]

    def album(self, str):
        for album in self.model.albums.albums:
            if str == album.__str__():
                return album
        return None

    def remove(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)
        self.set_button_state()

    def view(self):
        item = self.tree.item(self.tree.selection()[0], option="values")[0]
        chosen_album = self.album(item)
        AlbumView(Toplevel(), chosen_album).control()

    def close(self):
        self.root.destroy()

def seeded_record_store():
    return RecordStore(Albums(albums=[
        Album("Mayumi", "Serenity", 12, 34.99, "image/Serenity.png"),
        Album("Takio Senzu", "Oceans", 12, 34.99, "image/Oceans.png"),
        Album("Haru Yelin", "Alive", 12, 29.99, "image/Alive.png"),
        Album("Mayumi", "Arblard", 12, 29.99, "image/Arblard.png"),
        Album("Rin Kadoshi", "Lost", 12, 29.99, "image/Lost.png")
    ]))

if __name__ == "__main__":
    root = Tk()
    root.title("Record Store")
    RecordStoreView(root, seeded_record_store()).control()
    root.mainloop()