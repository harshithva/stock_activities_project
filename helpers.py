import csv
from db import Database
from tkinter import messagebox
db = Database('store.db')


class Helper:
    def getData(self):
        # oldest transaction date & format text
        oldest_transaction = ", ".join(db.oldest_transaction_date()[0][:5])
        self.oldest_transaction_date_label.config(
            text=f"Oldest Transaction date: {oldest_transaction}")
        # newest transaction date & format text
        newest_transaction = ", ".join(db.newest_transaction_date()[0][:5])
        self.newest_transaction_date_label.config(
            text=f"Newest Transaction date: {newest_transaction}")
        # delete existing
        for i in self.treeview1.get_children():
            self.treeview1.delete(i)
        # get unique stock symbols & populate
        symbols_count = 0
        for row in db.get_unique_stock_symbols():
            self.treeview1.insert("", 'end',
                                  values=row)
            symbols_count += 1
        self.no_unique_stocks_label.config(
            text=f"Number of unique stock symbols: {symbols_count}")
        # Cheapest stock
        cheapest_stock = db.get_cheapest_stock()[0]
        self.cheapest_stock_label.config(
            text=f"Cheapest stock: {cheapest_stock[0]} (Price - ${cheapest_stock[1]})")
        # Expensive stock
        expensive_stock = db.get_expensive_stock()[0]
        self.expensive_stock_label.config(
            text=f"Cheapest stock: {expensive_stock[0]} (Price - ${expensive_stock[1]})")
        # Most Traded stock
        most_traded_stock = db.get_most_traded_stock()[0]
        self.most_traded_stock_label.config(
            text=f"Most traded stock: {most_traded_stock[0]} ({most_traded_stock[1]} times)")

    def save_csv(self):
        text_file = open("stock_activity.txt", "w")
        for row in db.fetch():
            line = ' '.join(str(x) for x in row)
            text_file.write(line + '\n')
        text_file.close()
        messagebox.showinfo(
            'Success', 'TXT file exported successfully! Check your folder')
