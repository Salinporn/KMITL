import sys
from PySide6.QtCore import QByteArray
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from datetime import date as Date

class BookingSystem(object):
    def __init__(self):
        self.observers: list[BookingObserver] = []
        self.bookings = {}

    def addObserver(self, o):
        self.observers.append(o)

    def notifyObservers(self, data):
        for o in self.observers:
            o.update(data)

    def addBooking(self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]

    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k, v))
        self.notifyObservers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)

class BookingObserver(object):
    def update(self, data):
        pass

class StaffUI(BookingObserver, QWidget):
    def __init__(self, s, name):
        super().__init__()
        self.name = name
        self.system = s

        self.setWindowTitle('Booking List')
        self.setGeometry(300, 300, 300, 200)
        self.vbox = QVBoxLayout()

        self.bookinglist = QListWidget(self)
        self.vbox.addWidget(self.bookinglist)
        
        self.selectBookingButton = QPushButton("Select Booking...", self)
        self.selectBookingButton.clicked.connect(self.selectBooking)
        self.vbox.addWidget(self.selectBookingButton)

        self.setLayout(self.vbox)
    
    def update(self, bookings):
        print(self.name + ": StaffUI.update():")
        print("-- Booking Data --")
        self.bookinglist.clear()
        for data in bookings:
            items = data[1]
            for item in items:
                print(str(data[0]) + ": " + item)
                self.bookinglist.addItem(str(data[0]) + ": " + item)

    def selectBooking(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Select Booking')
        dialog.setGeometry(300, 300, 300, 200)
        vbox = QVBoxLayout()

        datelabel = QLabel(self)
        datelabel.setText("Date")
        vbox.addWidget(datelabel)
        self.date = QLineEdit(self)
        vbox.addWidget(self.date)

        monthlabel = QLabel(self)
        monthlabel.setText("Month")
        vbox.addWidget(monthlabel)
        self.month = QLineEdit(self)
        vbox.addWidget(self.month)

        yearlabel = QLabel(self)
        yearlabel.setText("Year")
        vbox.addWidget(yearlabel)
        self.year = QLineEdit(self)
        vbox.addWidget(self.year)

        submitButton = QPushButton("Submit", self)
        submitButton.clicked.connect(self.submitDate)
        vbox.addWidget(submitButton)
        dialog.setLayout(vbox)
        dialog.show()

    def submitDate(self):
        date = Date(int(self.year.text()), int(self.month.text()), int(self.date.text()))
        self.system.display(date)

    def submit(self, date):
        self.system.display(date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = BookingSystem()
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")

    ui1 = StaffUI(s, "UI#1")
    s.addObserver(ui1)
    ui1.submit(Date(2011, 10, 1))
    ui1.show()
    sys.exit(app.exec())
