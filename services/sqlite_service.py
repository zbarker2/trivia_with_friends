import sqlite3


class SQLiteService:
    def __init__(self):
        pass

    def connect(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def init_db(self):
        SCHEMA = """
        CREATE TABLE questions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value NUMBER NOT NULL,
            answer TEXT NOT NULL,
            question TEXT NOT NULL,
            positionData TEXT NOT NULL
        )
        CREATE TABLE teams(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            points NUMBER NOT NULL
        )
        CREATE TABLE categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
        """
        self.cursor.execute(SCHEMA)
