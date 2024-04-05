import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *

class TrafficLight:
    def __init__(self):
        self.current_color = "red"
        self.number = 4

    def changeColor(self, color):
        self.current_color = color
    
    def tick(self):
        if self.number == 1:
            if self.current_color == "red":
                self.changeColor("green")
                self.number = 3
            elif self.current_color == "green":
                self.changeColor("yellow")
                self.number = 2
            elif self.current_color == "yellow":
                self.changeColor("red")
                self.number = 4
        else:
            self.number -= 1

    def getNumber(self):
        return self.number
    
    def getState(self):
        return self.current_color


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traffic Light Demo")
        self.setGeometry(100, 100, 300, 100)
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()
        self.traffic_light = TrafficLight()

        self.button_red = QPushButton("")
        self.button_red.clicked.connect(self.flash_red)
        layout.addWidget(self.button_red,0,0)

        self.button_yellow = QPushButton("")
        self.button_yellow.clicked.connect(self.flash_yellow)
        layout.addWidget(self.button_yellow,0,1)

        self.button_green = QPushButton("")
        self.button_green.clicked.connect(self.flash_green)
        layout.addWidget(self.button_green,0,2)

        self.label_number = QLabel("Time: 4")
        layout.addWidget(self.label_number,1,0,1,3)

        self.setLayout(layout)

        # Timer to update the number every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_number)
        self.timer.start(1000)

        self.flash_red()

    def flash_red(self):
        self.button_red.setStyleSheet("background-color: #FF0000")
        self.button_yellow.setStyleSheet("background-color: None")
        self.button_green.setStyleSheet("background-color: None")
        QApplication.processEvents()

    def flash_yellow(self):
        self.button_red.setStyleSheet("background-color: None")
        self.button_yellow.setStyleSheet("background-color: #FFFF00")
        self.button_green.setStyleSheet("background-color: None")
        QApplication.processEvents()

    def flash_green(self):
        self.button_red.setStyleSheet("background-color: None")
        self.button_yellow.setStyleSheet("background-color: None")
        self.button_green.setStyleSheet("background-color: #00FF00")
        QApplication.processEvents()

    def update_number(self):
        self.traffic_light.tick()
        if self.traffic_light.getState() == "red":
            self.flash_red()
        elif self.traffic_light.getState() == "yellow":
            self.flash_yellow()
        elif self.traffic_light.getState() == "green":
            self.flash_green()
        self.label_number.setText("Time: {}".format(self.traffic_light.getNumber()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())