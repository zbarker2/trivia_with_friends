from PyQt6.QtWidgets import QPushButton


class QuestionButton(QPushButton):
    def __init__(self, question_id, is_active=True):
        super().__init__()
        self.is_active = is_active
        self.setText(f"test{question_id}")
        self.setObjectName(f"test{question_id}")
        self.setFixedSize(200, 100)
