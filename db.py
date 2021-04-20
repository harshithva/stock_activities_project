import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, date text, symbol text, t_type text, qty text, price text)")
        self.conn.commit()

    def fakeData():
        db = Database('store.db')
        db.insert("2021-04-20", "AMZN", "SELL", "10", "200")
        db.insert("2021-04-19", "AMZN", "BUY", "30", "478")
        db.insert("2021-04-18", "AMZN", "BUY", "30", "478")
        db.insert("2021-04-17", "AMZN", "SELL", "20", "478")
        db.insert("2021-04-16", "AMZN", "SELL", "20", "200")
        db.insert("2021-04-15", "AMZN", "SELL", "10", "600")

    def fetch(self):
        self.cur.execute("SELECT * FROM activities")
        rows = self.cur.fetchall()
        return rows

    def insert(self, date, symbol, t_type, qty, price):
        self.cur.execute("INSERT INTO activities VALUES (NULL, ?, ?, ?, ?, ?)",
                         (date, symbol, t_type, qty, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM activities WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE activities SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
