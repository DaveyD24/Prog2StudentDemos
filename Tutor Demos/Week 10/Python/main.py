from tkinter import *
from view.record_store_view import RecordStoreView
from model.record_store import RecordStore
from model.album import Album

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
    root = Tk()
    RecordStoreView(root, seeded_record_store())
    root.mainloop()