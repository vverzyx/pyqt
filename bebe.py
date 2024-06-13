from PyQt5.QtWidgets import (
   QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
   )

app = QApplication ([])

win = QWidget()
win.resize(700,500)

lineH = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

b1 = QPushButton("11111") 
b2 = QPushButton("22222")
b3 = QPushButton("33333")

lineV1.addWidget(b1)
lineV1.addWidget(b2)
lineV2.addWidget(b3)

lineH.addLayout(lineV1)
lineH.addLayout(lineV2)

win.setLayout(lineH)



win.show()
app.exec_()