import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, date text, symbol text, t_type text, qty text, price text)")
        self.conn.commit()

    def fakeData(self):
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

    def search(self, date, symbol, t_type, qty, price):
        query = f"SELECT * FROM activities WHERE date='{date}' AND symbol='{symbol}' AND t_type='{t_type}' AND qty='{qty}' AND price='{price}'"
        self.cur.execute(query)
        self.conn.commit()
        rows = self.cur.fetchall()
        return rows

    def oldest_transaction_date(self):
        query = "SELECT MIN(date), symbol FROM activities"
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def newest_transaction_date(self):
        query = "SELECT MAX(date), symbol FROM activities"
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def get_unique_stock_symbols(self):
        query = "SELECT DISTINCT symbol FROM activities"
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def get_cheapest_stock(self):
        query = "SELECT symbol, MIN(price) FROM activities"
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def get_expensive_stock(self):
        query = "SELECT symbol, MAX(price) FROM activities"
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def get_most_traded_stock(self):
        query = "SELECT  `symbol`, COUNT(`symbol`) AS `value_occurrence` FROM  `activities` GROUP BY `symbol` ORDER BY `value_occurrence` DESC LIMIT 1"
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def __del__(self):
        self.conn.close()
