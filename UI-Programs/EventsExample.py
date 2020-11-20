from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('Click here')

def on_button_clicked():
    m_box = QMessageBox()

    m_box.setText('Button clicked')
    m_box.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close)
    m_box.setDefaultButton(QMessageBox.Close)
    m_box.exec()

button.clicked.connect(on_button_clicked)
button.show()

app.exec()