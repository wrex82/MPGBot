import sqlite3


class Database:
    def __init__(self):
        self.name = 'mpgbot.db'
        self.connection = sqlite3.connect(self.name)
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS orders (\
            id INT,\
            type VARCHAR(16),\
            side VARCHAR(5),\
            price REAL,\
            quantity REAL,\
            status VARCHAR(10),\
            timestamp INT,\
            PRIMARY KEY (id)\
        )")
        self.connection.commit()
        cursor.close()

    def __str__(self):
        return "{name:" + self.name + "}"

    def close_connection(self):
        self.connection.close()
        self.connection = None

    def save_order(self, order):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO orders VALUES (%s, '%s', '%s', %s, %s, '%s', %s)" % (
            order['id'], order['type'], order['side'], order['price'], order['amount'], order['status'], order['timestamp']))
        self.connection.commit()
        cursor.close()

    def read_orders(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        cursor.close()

        return orders

    def clear_orders(self, ids=[]):
        cursor = self.connection.cursor()
        if len(ids) <= 0:
            cursor.execute("DELETE FROM orders")
        else:
            for id in ids:
                cursor.execute("DELETE FROM orders WHERE id='%s'" % id)

        self.connection.commit()
        cursor.close()