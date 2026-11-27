import sqlite3

from data_classes.question import Question


class QueryService:
    def __init__(self, cursor: sqlite3.Cursor):
        self.cursor = cursor

    def get_question_data(self, position_data) -> Question | None:
        result = self.cursor.execute(
            "SELECT * FROM questions WHERE positionData = ?",
            (position_data,),
        )
        raw = result.fetchone()

        if raw is None:
            return None

        question_data = Question(
            id=raw["id"],
            value=raw["value"],
            answer=raw["answer"],
            question=raw["question"],
            positionData=raw["positionData"],
        )

        return question_data

    def insert_quesiton_data(self, quesiton_data):
        return
