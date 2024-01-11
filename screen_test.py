import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import level1_snake
import level2_snake
import level3_snake

class GameWindow(QWidget):
    def __init__(self, level):
        super().__init__()
        self.setWindowTitle(f"Game Level {level}")
        self.setGeometry(100, 100, 400, 300)
        self.label = QLabel(f"Welcome to Game Level {level}!", self)
        self.label.move(100, 100)
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Menu")
        self.setGeometry(100, 100, 400, 300)
        self.button_level_1 = QPushButton("Level 1", self)
        self.button_level_1.move(100, 100)
        self.button_level_1.clicked.connect(lambda: self.level_1(1))
        self.button_level_2 = QPushButton("Level 2", self)
        self.button_level_2.move(100, 150)
        self.button_level_2.clicked.connect(lambda: self.level_2(2))
        self.button_level_3 = QPushButton("Level 3", self)
        self.button_level_3.move(100, 200)
        self.button_level_3.clicked.connect(lambda: self.level_3(3))
        self.show()

    def level_1(self, level):
        game = level1_snake.Level1()
        game.run()

    def level_2(self, level):
        game = level2_snake.Level2()
        game.run()

    def level_3(self, level):
        game = level3_snake.Level3()
        game.run()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
