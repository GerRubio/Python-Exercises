from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtGui

import os

file_path = None

app = QApplication([])

app.setApplicationName('C-LM Pad')
app.setWindowIcon(QtGui.QIcon('/home/gerardo/Python/Ejercicios/Python-Exercises/UI-Programs/Notepad/notepad_icon.png'))

class MainWindow(QMainWindow):
    def closeEvent(self, evt):
        answer = QMessageBox.question(
            window_area,
            'Confirmation', 
            'You have changes without save. Are you sure?',
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Save
        )

        if answer == QMessageBox.Save:
            save_file()
        elif answer == QMessageBox.Discard:
            evt.accept()
        else:
            evt.ignore()

text_area = QPlainTextEdit() 
window_area = MainWindow()

window_area.resize(720, 360)
window_area.setCentralWidget(text_area)

menu_bar = window_area.menuBar()
archive_bar = menu_bar.addMenu('File')
about_bar = menu_bar.addMenu('Help')
new_action = QAction('&New')
open_action = QAction('&Open')
save_action = QAction('&Save')
save_as_action = QAction('&Save as...')
about_action = QAction('&About')
close_action = QAction('&Close')

def show_open_dialog():
    global file_path
    
    file_name, _ = QFileDialog.getOpenFileName(
        window_area, 
        'Open fle...', 
        os.getcwd(), 
        'Text files (*.txt *.py)'
    )

    if file_name:
        with open(file_name, 'r') as f:
            text_area.setPlainText(f.read())
        
        file_path = file_name

def show_save_dialog():
    global file_path

    file_name, _ = QFileDialog.getSaveFileName(
        window_area, 
        'Save file...', 
        os.getcwd(), 
        'Text files (*.txt *.py)'
    )
    
    if file_name:
        with open(file_name, 'w') as f:
            f.write(text_area.toPlainText()) 
        
        file_path = file_name

def new_file():
    global file_path
    
    text_area.clear()

    file_path = None

def save_file():
    if file_path:
        with open(file_path, 'w') as f:
            f.write(text_area.toPlainText())
    else:
        show_save_dialog()

def show_about_dialog():
    text_info = """   
        <h2>C-LM Pad</h2>
        <h4>Version 0.0.1</h4>
        <p>Copyright EOI 2020<p>       
    """
    
    QMessageBox.about(window_area, 'About C-LM Pad...', text_info)

new_action.triggered.connect(new_file)
new_action.setShortcut(QKeySequence.New)

open_action.triggered.connect(show_open_dialog)
open_action.setShortcut(QKeySequence.Open)

save_action.triggered.connect(save_file)
save_action.setShortcut(QKeySequence.Save)

save_as_action.triggered.connect(show_save_dialog)
save_as_action.setShortcut(QKeySequence.SaveAs)

about_action.triggered.connect(show_about_dialog)
about_action.setShortcut(QKeySequence('Ctrl+I'))

close_action.triggered.connect(window_area.close)
close_action.setShortcut(QKeySequence('Ctrl+Q'))

archive_bar.addAction(new_action)
archive_bar.addAction(open_action)
archive_bar.addAction(save_action)
archive_bar.addAction(save_as_action)
archive_bar.addAction(close_action)
about_bar.addAction(about_action)

window_area.show()

app.exec()