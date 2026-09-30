from tkinter import *
from view.record_store_view import RecordStoreView
from model.record_store import RecordStore

if __name__ == "__main__":
    root = Tk()
    RecordStoreView(root, RecordStore())
    root.mainloop()