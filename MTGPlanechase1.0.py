
from genericpath import isdir
from numpy import indices
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QTransform, QIcon
from PyQt5.QtCore import Qt

import sys
import os
import random

class MainWindow(QWidget):
    cards = []
    deck = ""
    indices = []
    passed = 0

    def loadImages(self):
        if os.path.exists('assets'):
            os.chdir('assets')
        dir_contents = [os.path.abspath(file) 
            for file in os.listdir()]
        os.chdir(os.curdir)
        self.indices = [i for i in range(len(dir_contents))]
        for image_file in dir_contents:
            card = QPixmap(image_file)
            card = card.scaledToHeight(700)
            card = card.transformed(QTransform().rotate(90))
            self.cards.append(card)

    def draw(self):
        card = self.cards.pop(0)
        self.cards.append(card)
        self.deck.setPixmap(card)
        self.passed += 1

    def shuffle(self):
        random.shuffle(self.indices)
        temp_cards = [self.cards[i] for i in self.indices]
        self.cards = temp_cards
        self.deck.setPixmap(self.cards[0])
        self.passed = 0

    def undo(self):
        if self.passed > 0:
            card = self.cards.pop(len(self.cards) - 1)
            self.cards.insert(0, card)
            self.deck.setPixmap(card)
            self.passed -= 1

    def __init__(self):
        super().__init__()

        if os.path.exists('assets'):
            os.chdir('assets')
        self.setWindowIcon(QIcon('planeswalker.ico'))

        self.setWindowTitle("MTG Planechase")
        grid = QGridLayout()
        self.setLayout(grid)
        self.deck = QLabel(self)
        shuffle = QPushButton("Shuffle")
        shuffle.clicked.connect(self.shuffle)
        draw = QPushButton("Draw")
        draw.clicked.connect(self.draw)
        undo = QPushButton("Undo")
        undo.clicked.connect(self.undo)

        grid.addWidget(self.deck, 0, 0, 1, 3)
        grid.addWidget(shuffle, 1, 0)
        grid.addWidget(draw, 1, 1)
        grid.addWidget(undo, 1, 2)

        self.loadImages()
        self.draw()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()