import tkinter as tk
import tkinter.ttk as ttk
from db import Database

db = Database('store.db')


class ActivitesApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = ttk.Frame(self.toplevel1)
        self.label1 = ttk.Label(self.frame2)
        self.label1.configure(text='Date')
        self.label1.grid(column='0', pady='20', row='0')
        self.entry1 = ttk.Entry(self.frame2)
        _text_ = '''2021-04-20'''
        self.entry1.delete('0', 'end')
        self.entry1.insert('0', _text_)
        self.entry1.grid(column='0', row='1')
        self.label2 = ttk.Label(self.frame2)
        self.label2.configure(text='Symbol')
        self.label2.grid(column='1', row='0')
        self.entry2 = ttk.Entry(self.frame2)
        self.entry2.configure(exportselection='true')
        _text_ = '''Symbol'''
        self.entry2.delete('0', 'end')
        self.entry2.insert('0', _text_)
        self.entry2.grid(column='1', row='1')
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(text='Transaction Type')
        self.label3.grid(column='2', row='0')
        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(values='BUY SELL')
        self.combobox1.grid(column='2', row='1')
        self.label4 = ttk.Label(self.frame2)
        self.label4.configure(text='Quantity')
        self.label4.grid(column='3', row='0')
        self.entry3 = ttk.Entry(self.frame2)
        _text_ = '''0'''
        self.entry3.delete('0', 'end')
        self.entry3.insert('0', _text_)
        self.entry3.grid(column='3', row='1')
        self.label5 = ttk.Label(self.frame2)
        self.label5.configure(text='Price')
        self.label5.grid(column='4', row='0')
        self.entry4 = ttk.Entry(self.frame2)
        _text_ = '''0'''
        self.entry4.delete('0', 'end')
        self.entry4.insert('0', _text_)
        self.entry4.grid(column='4', row='1')

        self.record_button = ttk.Button(self.frame2)
        self.record_button.configure(text='Record')
        self.record_button.grid(column='0', columnspan='3', pady='20', row='3')
        self.record_button.configure(command=self.record)
        self.clear_button = ttk.Button(self.frame2)
        self.clear_button.configure(text='Clear')
        self.clear_button.grid(column='1', columnspan='3', row='3')
        self.clear_button.configure(command=self.clear)
        self.search_button = ttk.Button(self.frame2)
        self.search_button.configure(text='Search')
        self.search_button.grid(column='2', columnspan='3', row='3')
        self.search_button.configure(command=self.search)
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1_cols = ['column1', 'column2',
                               'column3', 'column4', 'column5']
        self.treeview1_dcols = ['column1', 'column2',
                                'column3', 'column4', 'column5']
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
        self.treeview1.heading('column1', anchor='w', text='Date')
        self.treeview1.heading('column2', anchor='w', text='Symbol')
        self.treeview1.heading('column3', anchor='w', text='Transaction Type')
        self.treeview1.heading('column4', anchor='w', text='Quantity')
        self.treeview1.heading('column5', anchor='w', text='Price')
        self.treeview1.grid(column='0', columnspan='5', row='4')
        self.frame2.configure(height='480', width='640')
        self.frame2.pack(side='top')
        self.toplevel1.configure(height='200', width='200')

        # Main widget
        self.mainwindow = self.toplevel1

    def record(self):
        print("Record")

    def clear(self):
        print("clear")

    def search(self):
        print("search")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = ActivitesApp()
    app.run()
