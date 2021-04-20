import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, date text, symbol text, type text, qty text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM activities")
        rows = self.cur.fetchall()
        return rows

    def insert(self, date, symbol, type, qty, price):
        self.cur.execute("INSERT INTO activities VALUES (NULL, ?, ?, ?, ?, ?)",
                         (date, symbol, type, qty, price))
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


db = Database('store.db')
db.insert("2021-04-20", "AMZN", "SELL", "10", "200")
