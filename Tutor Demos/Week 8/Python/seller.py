from tkinter import *

class Seller:
    SALE_PRICE = 34.99
    def __init__(self, root):
        self.root = root
        self.album_lbl = Label(self.root, text="Serenity")
        self.amount_entry = Entry(self.root)
        self.buy_btn = Button(self.root, text="Buy", command=self.sell)
        self.profit_lbl = Label(self.root, text="Profit: ")
        self.profit_txt = Label(self.root, text="0")

        self.album_lbl.pack(side=LEFT, padx=5)
        self.amount_entry.pack(side=LEFT, padx=5)
        self.buy_btn.pack(side=LEFT, padx=5)
        self.profit_lbl.pack(side=LEFT, padx=5)
        self.profit_txt.pack(side=LEFT, padx=5)

    def get_amount(self):
        return float(self.amount_entry.get())

    def get_current_profit(self):
        return float(self.profit_txt.cget("text"))

    def sell(self):
        sale = self.get_amount() * Seller.SALE_PRICE
        total_profit = self.get_current_profit() + sale
        self.profit_txt.config(text=f"{total_profit:.2f}")

if __name__ == "__main__":
    root = Tk()
    root.title("Seller")
    Seller(root)
    root.mainloop()