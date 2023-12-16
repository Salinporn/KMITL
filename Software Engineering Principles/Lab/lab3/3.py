import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import PySide6.QtWidgets
from program3_3 import Ui_MainWindow

class Phone(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.label = ""
        self.ui.button1.clicked.connect(self.display)
        self.ui.button2.clicked.connect(self.display)
        self.ui.button3.clicked.connect(self.display)
        self.ui.button4.clicked.connect(self.display)
        self.ui.button5.clicked.connect(self.display)
        self.ui.button6.clicked.connect(self.display)
        self.ui.button7.clicked.connect(self.display)
        self.ui.button8.clicked.connect(self.display)
        self.ui.button9.clicked.connect(self.display)
        self.ui.button0.clicked.connect(self.display)
        self.ui.button_star.clicked.connect(self.display)
        self.ui.button_square.clicked.connect(self.display)
        self.ui.del_button.clicked.connect(self.delete)
        self.ui.talk_button.clicked.connect(self.talk)
        

    def display(self):
        self.label += self.sender().text()
        self.ui.lineEdit.setText(self.label)
    
    def talk(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(f"Dialling {self.label}")
        layout.addWidget(label)

        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    def delete(self):
        self.label = self.label[:-1]
        self.ui.lineEdit.setText(self.label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Phone()
    w.show()
    sys.exit(app.exec())