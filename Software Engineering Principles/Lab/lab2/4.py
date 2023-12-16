import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Convert_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Amount of Money: ")
        vbox.addWidget(self.label)

        self.money = QLineEdit(self)
        vbox.addWidget(self.money)

        pbt1 = QPushButton("THB to USD", self)
        pbt1.clicked.connect(self.convert_to_usd)
        vbox.addWidget(pbt1)

        pbt2 = QPushButton("USD to THB", self)
        pbt2.clicked.connect(self.convert_to_thb)
        vbox.addWidget(pbt2)

        self.setLayout(vbox)
        self.show()

    def convert_to_usd(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(f"THB: {float(self.money.text()) / 30 : .2f}")
        layout.addWidget(label)

        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    def convert_to_thb(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(f"THB: {float(self.money.text()) * 30 : .2f}")
        layout.addWidget(label)

        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Convert_window()

    sys.exit(app.exec())