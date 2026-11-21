from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QWidget

from helpers.question_button import QuestionButton


class GameScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trivia With Friends")
        self.setFixedSize(800, 600)

        # Title Label section
        title = QLabel("GameScreen")
        title.setObjectName("titleText")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFrameShape(QFrame.Shape.NoFrame)

        # Exit button Settings
        exit_button = QPushButton("Exit")
        exit_button.setObjectName("startPageButton")
        exit_button.setFixedSize(200, 50)
        exit_button.clicked.connect(self.close)

        # Window Layout
        layout = QVBoxLayout()
        layout.addWidget(title, stretch=3)

        for i in range(5):
            question_button = QuestionButton(question_id=i)
            layout.addWidget(
                question_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0
            )
            if i < 4:
                layout.addSpacing(8)
        self.setLayout(layout)
