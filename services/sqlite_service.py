import sqlite3

class SQLiteService:
    def __init__(self):
        pass
    def connect (self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        