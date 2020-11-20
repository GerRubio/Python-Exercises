from PyQt5.QtWidgets import *
from PyQt5 import QtCore 

app = QApplication([])

window = QWidget()
ext_layout = QVBoxLayout()
inter_layout = QHBoxLayout()
label_x = QLabel('Label X')
label_y = QLabel('Label Y')

ext_layout.addLayout(inter_layout)

inter_layout.addWidget(label_x)
label_x.setAlignment(QtCore.Qt.AlignCenter)

inter_layout.addWidget(label_y)
label_y.setAlignment(QtCore.Qt.AlignCenter)

ext_layout.addWidget(QPushButton('Click here'))

window.setLayout(ext_layout)

window.show()
app.exec()