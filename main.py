import tkinter as tk
import tkinter.ttk as ttk
from db import Database
from activities import ActivitesApp

db = Database('store.db')


def getData(self):
    # oldest transaction date & format text
    oldest_transaction = ", ".join(db.oldest_transaction_date()[0][:5])
    self.oldest_transaction_date_label.config(
        text=f"Oldest Transaction date: {oldest_transaction}")
    # newest transaction date & format text
    newest_transaction = ", ".join(db.newest_transaction_date()[0][:5])
    self.newest_transaction_date_label.config(
        text=f"Newest Transaction date: {newest_transaction}")
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


class SummaryApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel2 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame10 = ttk.Frame(self.toplevel2)
        self.frame11 = ttk.Frame(self.frame10)

        self.summary_button = ttk.Button(self.frame11)
        self.summary_button.configure(text='Summary')
        self.summary_button.grid(column='0', padx='10', pady='10', row='0')

        self.activities_button = ttk.Button(self.frame11)
        self.activities_button.configure(text='Activities')
        self.activities_button.grid(column='1', row='0')
        self.activities_button.configure(command=self.openActivitiesWindow)

        self.frame11.configure(height='200', width='200')
        self.frame11.grid(column='0', pady='10', row='0')

        self.oldest_transaction_date_label = ttk.Label(self.frame10)
        self.oldest_transaction_date_label.configure(
            relief='groove', text='Oldest Transaction  Date: 21-04-21(AMAZN)')
        self.oldest_transaction_date_label.grid(column='0', pady='20', row='1')

        self.newest_transaction_date_label = ttk.Label(self.frame10)
        self.newest_transaction_date_label.configure(
            relief='groove', text='Newest Transaction Date: 21-04-21(AMAZN)')
        self.newest_transaction_date_label.grid(
            column='0', padx='10', pady='10', row='2')

        self.no_unique_stocks_label = ttk.Label(self.frame10)
        self.no_unique_stocks_label.configure(
            relief='groove', text='Number of unique stock symbols - 20')
        self.no_unique_stocks_label.grid(column='0', pady='10', row='5')

        self.treeview1 = ttk.Treeview(self.frame10)
        self.treeview1_cols = ['column1']
        self.treeview1_dcols = ['column1']
        self.treeview1.configure(
            columns=self.treeview1_cols, displaycolumns=self.treeview1_dcols)
        self.treeview1.column('column1', anchor='w',
                              stretch='true', width='200', minwidth='20')
        self.treeview1.heading('column1', anchor='w', text='Symbol')
        self.treeview1.grid(column='1', row='5')

        self.cheapest_stock_label = ttk.Label(self.frame10)
        self.cheapest_stock_label.configure(
            relief='groove', text='Cheapest stock: AMZN')
        self.cheapest_stock_label.grid(column='0', pady='10', row='7')

        self.expensive_stock_label = ttk.Label(self.frame10)
        self.expensive_stock_label.configure(
            relief='groove', text='Most expensive stock: AMAZN')
        self.expensive_stock_label.grid(column='0', pady='10', row='8')

        self.most_traded_stock_label = ttk.Label(self.frame10)
        self.most_traded_stock_label.configure(
            relief='groove', text='Most traded stock: AMZN')
        self.most_traded_stock_label.grid(column='0', pady='10', row='9')

        self.frame10.configure(height='200', width='200')
        self.frame10.pack(side='top')
        self.toplevel2.configure(height='480', width='640')

        # Main widget
        self.mainwindow = self.toplevel2

        getData(self)

    def openActivitiesWindow(self):
        ActivitesApp()

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = SummaryApp()
    app.run()
