import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class ToDoListsApp(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.task_list = QListWidget()
        vbox.addWidget(self.task_list)

        self.task_label = QLabel(self)
        self.task_label.setText("Task: ")
        vbox.addWidget(self.task_label)

        self.task = QLineEdit(self)
        vbox.addWidget(self.task)

        addBT = QPushButton("Add", self)
        addBT.clicked.connect(self.addTask)
        vbox.addWidget(addBT)

        removeBT = QPushButton("Remove", self)
        removeBT.clicked.connect(self.removeTask)
        vbox.addWidget(removeBT)

        closeBT = QPushButton("Close", self)
        closeBT.clicked.connect(self.close)
        vbox.addWidget(closeBT)

        self.setLayout(vbox)
        self.show()

    def addTask(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        status_label = QLabel(self)

        if self.task.text() == "":
            status_label.setText("Please enter a task.")
        else:
            self.task_list.addItem(self.task.text())
            status_label.setText(f"Successfully added.")
        layout.addWidget(status_label)
        self.task.setText("")

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(dialog.close)
        layout.addWidget(ok_button)
        dialog.setLayout(layout)
        dialog.show()

    def removeTask(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        status_label = QLabel(self)

        selected_item = self.task_list.currentItem()
        if self.task_list.count() == 0:
            status_label.setText("There is no task to remove.")
        elif selected_item is None:
            status_label.setText("Please select a task.")
        else:
            self.task_list.takeItem(self.task_list.row(selected_item))
            status_label.setText(f"Successfully removed.")
        layout.addWidget(status_label)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(dialog.close)
        layout.addWidget(ok_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = ToDoListsApp()
    w.setWindowTitle('To-Do List')

    sys.exit(app.exec())
