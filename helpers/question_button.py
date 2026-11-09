from PyQt6.QtWidgets import QPushButton

class QuestionButton(QPushButton):
    def __init__(self, value, question_text, question_answer, is_active=True):
        super(QuestionButton, self).__init__()
        self.value = value
        self.question_text = question_text
        self.question_answer = question_answer
        self.is_active = is_active
        self.setText(f"${self.value}")
    
            
    