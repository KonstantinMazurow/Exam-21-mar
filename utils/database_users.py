import sqlite3 as sql


class Database():
    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_users_id(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users_id (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user TEXT UNIQUE NOT NULL)
        ''')

    def insert_user_id(self, data):
        self.cur.execute('''INSERT or IGNORE INTO users_id
                            (id_user) VALUES (?)''', data)
        self.con.commit()

    def close(self):
        self.con.close()


db1 = Database('Users_id.db')
