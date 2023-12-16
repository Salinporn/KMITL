# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_3.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 709)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 471, 21))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 50, 141, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.button1 = QPushButton(self.verticalLayoutWidget)
        self.button1.setObjectName(u"button1")
        self.button1.setEnabled(True)
        font = QFont()
        font.setPointSize(36)
        self.button1.setFont(font)

        self.verticalLayout.addWidget(self.button1)

        self.button4 = QPushButton(self.verticalLayoutWidget)
        self.button4.setObjectName(u"button4")
        self.button4.setFont(font)

        self.verticalLayout.addWidget(self.button4)

        self.button7 = QPushButton(self.verticalLayoutWidget)
        self.button7.setObjectName(u"button7")
        self.button7.setFont(font)

        self.verticalLayout.addWidget(self.button7)

        self.button_star = QPushButton(self.verticalLayoutWidget)
        self.button_star.setObjectName(u"button_star")
        self.button_star.setFont(font)

        self.verticalLayout.addWidget(self.button_star)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(170, 50, 141, 311))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button2 = QPushButton(self.verticalLayoutWidget_2)
        self.button2.setObjectName(u"button2")
        self.button2.setEnabled(True)
        self.button2.setFont(font)

        self.verticalLayout_2.addWidget(self.button2)

        self.button5 = QPushButton(self.verticalLayoutWidget_2)
        self.button5.setObjectName(u"button5")
        self.button5.setFont(font)

        self.verticalLayout_2.addWidget(self.button5)

        self.button8 = QPushButton(self.verticalLayoutWidget_2)
        self.button8.setObjectName(u"button8")
        self.button8.setFont(font)

        self.verticalLayout_2.addWidget(self.button8)

        self.button0 = QPushButton(self.verticalLayoutWidget_2)
        self.button0.setObjectName(u"button0")
        self.button0.setFont(font)

        self.verticalLayout_2.addWidget(self.button0)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(330, 50, 151, 311))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button3 = QPushButton(self.verticalLayoutWidget_3)
        self.button3.setObjectName(u"button3")
        self.button3.setEnabled(True)
        self.button3.setFont(font)

        self.verticalLayout_3.addWidget(self.button3)

        self.button6 = QPushButton(self.verticalLayoutWidget_3)
        self.button6.setObjectName(u"button6")
        self.button6.setFont(font)

        self.verticalLayout_3.addWidget(self.button6)

        self.button9 = QPushButton(self.verticalLayoutWidget_3)
        self.button9.setObjectName(u"button9")
        self.button9.setFont(font)

        self.verticalLayout_3.addWidget(self.button9)

        self.button_square = QPushButton(self.verticalLayoutWidget_3)
        self.button_square.setObjectName(u"button_square")
        self.button_square.setFont(font)

        self.verticalLayout_3.addWidget(self.button_square)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 380, 471, 80))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.talk_button = QPushButton(self.horizontalLayoutWidget)
        self.talk_button.setObjectName(u"talk_button")
        self.talk_button.setFont(font)

        self.horizontalLayout_6.addWidget(self.talk_button)

        self.del_button = QPushButton(self.horizontalLayoutWidget)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setFont(font)

        self.horizontalLayout_6.addWidget(self.del_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 807, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_star.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_square.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.talk_button.setText(QCoreApplication.translate("MainWindow", u"Talk", None))
        self.del_button.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi

