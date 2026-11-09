
from PyQt6.QtWidgets import  QWidget, QPushButton, QVBoxLayout

class StartScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeopardy With Friends")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        