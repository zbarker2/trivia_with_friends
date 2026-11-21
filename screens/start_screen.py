from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QWidget

from screens.game_manager_screen import GameManagerScreen
from screens.game_screen import GameScreen


class StartScreen(QWidget):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowTitle("Trivia With Friends")
        self.setFixedSize(800, 600)

        # Title Label section
        title = QLabel("Trivia With Friends")
        title.setObjectName("titleText")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFrameShape(QFrame.Shape.NoFrame)

        # Create Game button Settings
        create_button = QPushButton("Create Game")
        create_button.setObjectName("startPageButton")
        create_button.setFixedSize(200, 50)
        create_button.clicked.connect(self.start_game)

        # Load Game button Settings
        load_button = QPushButton("Load Game")
        load_button.setObjectName("startPageButton")
        load_button.setFixedSize(200, 50)
        load_button.clicked.connect(self.load_game)

        # Exit button Settings
        exit_button = QPushButton("Exit")
        exit_button.setObjectName("startPageButton")
        exit_button.setFixedSize(200, 50)
        exit_button.clicked.connect(self.close)

        # Window Layout
        layout = QVBoxLayout()
        layout.addWidget(title, stretch=3)
        # layout.addStretch(0)
        layout.addSpacing(8)
        layout.addWidget(
            create_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0
        )
        layout.addSpacing(8)
        layout.addWidget(load_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        layout.addSpacing(8)
        layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter, stretch=0)
        layout.addSpacing(20)
        self.setLayout(layout)

    def start_game(self):
        self.game_manager_screen = GameManagerScreen()
        self.game_manager_screen.show()
        self.game_screen = GameScreen()
        self.game_screen.show()
        self.close()

    def load_game(self):
        print("Load Game")
