
from PyQt6.QtWidgets import  QWidget, QPushButton, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt

class StartScreen(QWidget):
    def __init__(self):
        super().__init__()

        #Window Settings
        self.setWindowTitle("Jeopardy With Friends")
        self.setFixedSize(800, 600)

        #Title Label section
        title = QLabel("Jeopardy With Friends")
        title.setObjectName("titleText")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFrameShape(QFrame.Shape.NoFrame)

        #Demo Game button Settings
        demo_button = QPushButton("Demo Game")
        demo_button.setObjectName("startPageButton")
        demo_button.setFixedSize(200, 50)
        demo_button.clicked.connect(self.start_game)

        #Create Game button Settings
        create_button = QPushButton("Create Game")
        create_button.setObjectName("startPageButton")
        create_button.setFixedSize(200, 50)
        create_button.clicked.connect(self.start_game)

        #Load Game button Settings
        load_button = QPushButton("Load Game")
        load_button.setObjectName("startPageButton")
        load_button.setFixedSize(200, 50)
        load_button.clicked.connect(self.load_game)

        #Exit button Settings
        exit_button = QPushButton("Exit")
        exit_button.setObjectName("startPageButton")
        exit_button.setFixedSize(200, 50)
        exit_button.clicked.connect(self.close)

        # Window Layout
        layout = QVBoxLayout()
        layout.addWidget(title,stretch=3)
        # layout.addStretch(0)
        layout.setSpacing(8)
        layout.addWidget(demo_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        layout.addWidget(create_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        layout.addWidget(load_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        layout.addSpacing(20)
        self.setLayout(layout)

    def start_game(self):
        print("Create Game")

    def load_game(self): 
        print("Load Game")