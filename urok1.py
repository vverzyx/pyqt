from PyQt5.QtWidgets import (
   QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from random import *

dodatok = QApplication([])
win = QWidget()
win.resize(400,300)

win.setWindowTitle("Визначник переможця")

nadp = QLabel("Натисни, щоб дізнатися переможця")
LineV = QVBoxLayout()
LineV.addWidget(nadp, alignment = Qt.AlignCenter)

nadp2 = QLabel("?")
LineV.addWidget(nadp2, alignment = Qt.AlignCenter)

knopka = QPushButton("Згенерувати")
LineV.addWidget(knopka, alignment = Qt.AlignCenter)

win.setLayout(LineV)

def one():
    nadp.setText("Переможець: ")
    nadp2.setText(str(randint(1,100)))

knopka.clicked.connect(one)

win.show()
dodatok.exec_()