import sys

from PyQt6.QtWidgets import QApplication

from screens.start_screen import StartScreen


def main():

    app = QApplication(sys.argv)
    with open("app_style.qss", "r") as f:
        style = f.read()
    app.setStyleSheet(style)
    start_screen = StartScreen()
    start_screen.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
