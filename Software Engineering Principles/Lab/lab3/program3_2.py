# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(8, 10, 191, 281))
        font = QFont()
        font.setPointSize(48)
        self.num_label.setFont(font)
        self.num_label.setLayoutDirection(Qt.LeftToRight)
        self.num_label.setTextFormat(Qt.MarkdownText)
        self.num_label.setAlignment(Qt.AlignCenter)
        self.num_label.setMargin(0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(189, 9, 201, 281))
        self.inc_button = QPushButton(self.widget)
        self.inc_button.setObjectName(u"inc_button")
        self.inc_button.setGeometry(QRect(0, 0, 201, 81))
        self.inc_button.setMaximumSize(QSize(201, 131))
        font1 = QFont()
        font1.setPointSize(25)
        self.inc_button.setFont(font1)
        self.dec_button = QPushButton(self.widget)
        self.dec_button.setObjectName(u"dec_button")
        self.dec_button.setGeometry(QRect(0, 90, 201, 81))
        self.dec_button.setMaximumSize(QSize(201, 131))
        self.dec_button.setFont(font1)
        self.reset_button = QPushButton(self.widget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(0, 180, 201, 91))
        self.reset_button.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:48pt;\">0</span></p></body></html>", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.dec_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

