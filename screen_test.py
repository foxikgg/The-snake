import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import Qt
import level1_snake
import level2_snake
import level3_snake


class GameWindow(QWidget):
    def __init__(self, level):
        super().__init__()
        self.setWindowTitle(f"Game Level {level}")
        self.setGeometry(50, 50, 100, 100)
        self.label = QLabel(f"Welcome to Game Level {level}!", self)
        self.label.move(100, 100)
        self.show()

class LevelDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Выберите уровень")
        self.setGeometry(100, 100, 400, 300)
        self.button_level_1 = QPushButton("Уровень 1", self)
        self.button_level_1.move(100, 100)
        self.button_level_1.clicked.connect(lambda: self.level_1(1))
        self.button_level_2 = QPushButton("Уровень 2", self)
        self.button_level_2.move(100, 150)
        self.button_level_2.clicked.connect(lambda: self.level_2(2))
        self.button_level_3 = QPushButton("Уровень 3", self)
        self.button_level_3.move(100, 200)
        self.button_level_3.clicked.connect(lambda: self.level_3(3))

    def level_1(self, level):
        game = level1_snake.Level1()
        game.run()


    def level_2(self, level):
        game = level2_snake.Level2()
        game.run()


    def level_3(self, level):
        game = level3_snake.Level3()
        game.run()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Menu")
        self.setGeometry(100, 100, 1280, 720)

        # Установка фонового изображения
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap("data/main_menu.png")))
        self.setPalette(palette)

        self.button_play = QPushButton("Играть", self)
        self.button_play.setGeometry(585, 450, 151, 36)
        self.button_play.setStyleSheet("""QPushButton {background-color: #10CF75; border-radius: 12px; color: #FFFFFF; 
            font-family : Alegreya Sans; font-weight : Bold; }""")
        self.button_play.clicked.connect(self.open_level_dialog)
        self.show()

    def open_level_dialog(self):
        self.level_dialog = LevelDialog(self)
        self.level_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
