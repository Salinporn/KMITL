import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import PySide6.QtWidgets
import random
from game import Ui_Form

class GuessNumberGame(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.num_label = ""
        self.to_guess_num = random.randint(1, 100)

        self.ui.button_easy.clicked.connect(self.set_level)
        self.ui.button_medium.clicked.connect(self.set_level)
        self.ui.button_hard.clicked.connect(self.set_level)

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

        self.ui.button_delete.clicked.connect(self.delete)
        self.ui.button_reset.clicked.connect(self.reset)
        self.ui.button_guess.clicked.connect(self.guess)

    def set_level(self):
        self.ui.number_input.setText("")
        self.num_label = ""

        if self.sender().text() == "Easy":
            self.to_guess_num = random.randint(1, 100)
            self.level_label = "Current Difficulty: Easy"
            self.rule_label = "The number is between 1-100"
        elif self.sender().text() == "Medium":
            self.to_guess_num = random.randint(1, 500)
            self.level_label = "Current Difficulty: Medium"
            self.rule_label = "The number is between 1-500"
        elif self.sender().text() == "Hard":
            self.to_guess_num = random.randint(1, 1000)
            self.level_label = "Current Difficulty: Hard"
            self.rule_label = "The number is between 1-1000"
            
        self.ui.level_label.setText(self.level_label)
        self.ui.rule_label.setText(self.rule_label)

    def display(self):
        self.num_label += self.sender().text()
        self.ui.number_input.setText(self.num_label)

    def delete(self):
        self.num_label = self.num_label[:-1]
        self.ui.number_input.setText(self.num_label)
    
    def reset(self):
        self.num_label = ""
        self.ui.number_input.setText(self.num_label)
    
    def guess(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)

        if self.num_label == "":
            label.setText("Please enter a number")
        elif int(self.num_label) == self.to_guess_num:
            label.setText(f"You win! The number was {self.to_guess_num}.")
            if self.level_label == "Current Difficulty: Easy":
                self.to_guess_num = random.randint(1, 100)
            elif self.level_label == "Current Difficulty: Medium":
                self.to_guess_num = random.randint(1, 500)
            elif self.level_label == "Current Difficulty: Hard":
                self.to_guess_num = random.randint(1, 1000)
        elif int(self.num_label) > self.to_guess_num:
            label.setText("Guess lower number")
        elif int(self.num_label) < self.to_guess_num:
            label.setText("Guess higher number")
        else:
            label.setText("Invalid input!")

        self.num_label = ""
        self.ui.number_input.setText(self.num_label)

        layout.addWidget(label)
        ok_button = QPushButton("Okay", self)
        ok_button.clicked.connect(dialog.close)
        layout.addWidget(ok_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GuessNumberGame()
    w.show()
    sys.exit(app.exec())
