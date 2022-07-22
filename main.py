from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MTG Planechase")
        grid = QGridLayout()
        self.setLayout(grid)

        card_image = QPixmap(r"C:\Users\Chuck\Desktop\Side Projects\mtg_planechase\assets\0b8a0cad-92df-45a1-a3cc-561be2f06778.jpg")
        card_image = card_image.scaledToHeight(700)
        card_image = card_image.transformed(QTransform().rotate(90))
        deck = QLabel(self)
        deck.setPixmap(card_image)
        shuffle = QPushButton("Shuffle")
        draw = QPushButton("Draw")
        undo = QPushButton("Undo")

        grid.addWidget(deck, 0, 0, 1, 3)
        grid.addWidget(shuffle, 1, 0)
        grid.addWidget(draw, 1, 1)
        grid.addWidget(undo, 1, 2)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()