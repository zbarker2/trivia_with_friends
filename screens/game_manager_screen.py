from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class GameManagerScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trivia With Friends")
        self.setFixedSize(800, 600)

        # Title Label section
        title = QLabel("Game Manager Screen")
        title.setObjectName("titleText")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFrameShape(QFrame.Shape.NoFrame)

        # Exit button Settings
        exit_button = QPushButton("Close All")
        exit_button.setObjectName("startPageButton")
        exit_button.setFixedSize(200, 50)
        exit_button.clicked.connect(QApplication.quit)
        # Window Layout
        layout = QVBoxLayout()
        layout.addWidget(title, stretch=3)
        # layout.addStretch(0)
        layout.setSpacing(8)
        layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        self.setLayout(layout)
