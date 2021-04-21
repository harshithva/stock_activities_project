import tkinter as tk
import tkinter.ttk as ttk
from db import Database
from tkinter import messagebox
from datetime import datetime

# from main import SummaryApp

db = Database('store.db')


def populate_list(self):
    # delete all
    for i in self.treeview1.get_children():
        self.treeview1.delete(i)
    # populate
    for row in db.fetch():
        self.treeview1.insert("", 'end',
                              values=row)


class ActivitesApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame1 = ttk.Frame(self.toplevel1)
        self.date_label = ttk.Label(self.frame1)
        self.date_label.configure(text='Date')
        self.date_label.grid(column='0', pady='20', row='0')

        self.date_entry = ttk.Entry(self.frame1)
        _text_ = datetime.today().strftime('%Y-%m-%d')
        self.date_entry.delete('0', 'end')
        self.date_entry.insert('0', _text_)
        self.date_entry.grid(column='0', row='1')

        self.symbol_label = ttk.Label(self.frame1)
        self.symbol_label.configure(text='Symbol')
        self.symbol_label.grid(column='1', row='0')

        self.symbol_entry = ttk.Entry(self.frame1)
        self.symbol_entry.configure(exportselection='true')
        _text_ = '''Symbol'''
        self.symbol_entry.delete('0', 'end')
        self.symbol_entry.insert('0', _text_)
        self.symbol_entry.grid(column='1', row='1')

        self.transaction_type_label = ttk.Label(self.frame1)
        self.transaction_type_label.configure(text='Transaction Type')
        self.transaction_type_label.grid(column='2', row='0')

        self.transaction_type_combobox = ttk.Combobox(self.frame1)
        self.transaction_type_combobox.configure(values='BUY SELL')
        self.transaction_type_combobox.grid(column='2', row='1')

        self.quantity_label = ttk.Label(self.frame1)
        self.quantity_label.configure(text='Quantity')
        self.quantity_label.grid(column='3', row='0')

        self.quantity_entry = ttk.Entry(self.frame1)
        _text_ = '''0'''
        self.quantity_entry.delete('0', 'end')
        self.quantity_entry.insert('0', _text_)
        self.quantity_entry.grid(column='3', row='1')

        self.price_label = ttk.Label(self.frame1)
        self.price_label.configure(text='Price')
        self.price_label.grid(column='4', row='0')

        self.price_entry = ttk.Entry(self.frame1)
        _text_ = '''0'''
        self.price_entry.delete('0', 'end')
        self.price_entry.insert('0', _text_)
        self.price_entry.grid(column='4', row='1')

        self.record_button = ttk.Button(self.frame1)
        self.record_button.configure(text='Record')
        self.record_button.grid(column='0', columnspan='3', pady='20', row='3')
        self.record_button.configure(command=self.record)
        self.clear_button = ttk.Button(self.frame1)
        self.clear_button.configure(text='Clear')
        self.clear_button.grid(column='1', columnspan='3', row='3')
        self.clear_button.configure(command=self.clear)
        self.search_button = ttk.Button(self.frame1)
        self.search_button.configure(text='Search')
        self.search_button.grid(column='2', columnspan='3', row='3')
        self.search_button.configure(command=self.search)

        self.treeview1 = ttk.Treeview(self.frame1)
        self.treeview1_cols = ['column1', 'column2',
                               'column3', 'column4', 'column5', 'column6']
        self.treeview1_dcols = ['column1', 'column2',
                                'column3', 'column4', 'column5', 'column6']
        self.treeview1.configure(
            columns=self.treeview1_cols, displaycolumns=self.treeview1_dcols)
        self.treeview1.column('column1', anchor='w',
                              stretch='true', width='200', minwidth='20')
        self.treeview1.column('column2', anchor='w',
                              stretch='true', width='200', minwidth='20')
        self.treeview1.column('column3', anchor='w',
                              stretch='true', width='200', minwidth='20')
        self.treeview1.column('column4', anchor='w',
                              stretch='true', width='200', minwidth='20')
        self.treeview1.column('column5', anchor='w',
                              stretch='true', width='200', minwidth='20')
        self.treeview1.heading('column1', anchor='w', text='ID')
        self.treeview1.heading('column2', anchor='w', text='Date')
        self.treeview1.heading('column3', anchor='w', text='Symbol')
        self.treeview1.heading('column4', anchor='w', text='Transaction Type')
        self.treeview1.heading('column5', anchor='w', text='Quantity')
        self.treeview1.heading('column6', anchor='w', text='Price')
        self.treeview1.grid(column='0', columnspan='5', row='4')

        self.frame1.configure(height='480', width='640')
        self.frame1.pack(side='top')
        self.toplevel1.configure(height='200', width='200')

        # Main widget
        self.mainwindow = self.toplevel1

        populate_list(self)

    def record(self):
        if self.date_entry.get() == '' or self.symbol_entry.get() == '' or self.transaction_type_combobox.get() == '' or self.quantity_entry.get() == '' or self.price_entry.get() == '':
            messagebox.showerror(
                'Required Fields', 'Please include all fields')
            return

        db.insert(self.date_entry.get(), self.symbol_entry.get(),
                  self.transaction_type_combobox.get(), self.quantity_entry.get(), self.price_entry.get())
        populate_list(self)

    def clear(self):
        self.date_entry.delete('0', 'end')
        self.symbol_entry.delete('0', 'end')
        self.transaction_type_combobox.delete('0', 'end')
        self.quantity_entry.delete('0', 'end')
        self.price_entry.delete('0', 'end')

    def search(self):
        # delete all
        for i in self.treeview1.get_children():
            self.treeview1.delete(i)
         # populate
        for row in db.search(self.date_entry.get(), self.symbol_entry.get(),
                             self.transaction_type_combobox.get(), self.quantity_entry.get(), self.price_entry.get()):
            self.treeview1.insert("", 'end',
                                  values=row)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = ActivitesApp()
    app.run()
