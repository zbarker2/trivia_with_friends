import sqlite3


class QueryService:
    def __init__(self, cursor: sqlite3.Cursor):
        self.cursor = cursor

    def get_question_data(self, position_data):
        result = self.cursor.execute(f"SELECT * FROM questions WHERE positionData == {position_data}")
        return result
    def insert_quesiton_data(self, quesiton_data):
        return
