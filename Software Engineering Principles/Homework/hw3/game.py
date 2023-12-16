# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(261, 391)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.game_label = QLabel(Form)
        self.game_label.setObjectName(u"game_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.game_label.sizePolicy().hasHeightForWidth())
        self.game_label.setSizePolicy(sizePolicy1)
        self.game_label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.game_label.setFont(font)
        self.game_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.game_label)

        self.level_label = QLabel(Form)
        self.level_label.setObjectName(u"level_label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.level_label.setFont(font1)
        self.level_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.level_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_easy = QPushButton(Form)
        self.button_easy.setObjectName(u"button_easy")
        font2 = QFont()
        font2.setPointSize(12)
        self.button_easy.setFont(font2)

        self.horizontalLayout.addWidget(self.button_easy)

        self.button_medium = QPushButton(Form)
        self.button_medium.setObjectName(u"button_medium")
        self.button_medium.setFont(font2)

        self.horizontalLayout.addWidget(self.button_medium)

        self.button_hard = QPushButton(Form)
        self.button_hard.setObjectName(u"button_hard")
        self.button_hard.setFont(font2)

        self.horizontalLayout.addWidget(self.button_hard)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.rule_label = QLabel(Form)
        self.rule_label.setObjectName(u"rule_label")
        font3 = QFont()
        font3.setPointSize(10)
        self.rule_label.setFont(font3)
        self.rule_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.rule_label)

        self.number_input = QLineEdit(Form)
        self.number_input.setObjectName(u"number_input")
        self.number_input.setFont(font2)
        self.number_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.number_input)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button7 = QPushButton(Form)
        self.button7.setObjectName(u"button7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(15)
        self.button7.setFont(font4)

        self.gridLayout_2.addWidget(self.button7, 3, 0, 1, 1)

        self.button2 = QPushButton(Form)
        self.button2.setObjectName(u"button2")
        sizePolicy2.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy2)
        self.button2.setFont(font4)

        self.gridLayout_2.addWidget(self.button2, 1, 1, 1, 1)

        self.button8 = QPushButton(Form)
        self.button8.setObjectName(u"button8")
        sizePolicy2.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy2)
        self.button8.setFont(font4)

        self.gridLayout_2.addWidget(self.button8, 3, 1, 1, 1)

        self.button1 = QPushButton(Form)
        self.button1.setObjectName(u"button1")
        sizePolicy2.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy2)
        self.button1.setFont(font4)

        self.gridLayout_2.addWidget(self.button1, 1, 0, 1, 1)

        self.button_delete = QPushButton(Form)
        self.button_delete.setObjectName(u"button_delete")
        sizePolicy2.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy2)
        self.button_delete.setFont(font2)

        self.gridLayout_2.addWidget(self.button_delete, 4, 2, 1, 1)

        self.button9 = QPushButton(Form)
        self.button9.setObjectName(u"button9")
        sizePolicy2.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy2)
        self.button9.setFont(font4)

        self.gridLayout_2.addWidget(self.button9, 3, 2, 1, 1)

        self.button4 = QPushButton(Form)
        self.button4.setObjectName(u"button4")
        sizePolicy2.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy2)
        self.button4.setFont(font4)

        self.gridLayout_2.addWidget(self.button4, 2, 0, 1, 1)

        self.button3 = QPushButton(Form)
        self.button3.setObjectName(u"button3")
        sizePolicy2.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy2)
        self.button3.setFont(font4)

        self.gridLayout_2.addWidget(self.button3, 1, 2, 1, 1)

        self.button_reset = QPushButton(Form)
        self.button_reset.setObjectName(u"button_reset")
        sizePolicy2.setHeightForWidth(self.button_reset.sizePolicy().hasHeightForWidth())
        self.button_reset.setSizePolicy(sizePolicy2)
        self.button_reset.setFont(font2)

        self.gridLayout_2.addWidget(self.button_reset, 4, 0, 1, 1)

        self.button5 = QPushButton(Form)
        self.button5.setObjectName(u"button5")
        sizePolicy2.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy2)
        self.button5.setFont(font4)

        self.gridLayout_2.addWidget(self.button5, 2, 1, 1, 1)

        self.button0 = QPushButton(Form)
        self.button0.setObjectName(u"button0")
        sizePolicy2.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy2)
        self.button0.setFont(font4)

        self.gridLayout_2.addWidget(self.button0, 4, 1, 1, 1)

        self.button6 = QPushButton(Form)
        self.button6.setObjectName(u"button6")
        sizePolicy2.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy2)
        self.button6.setFont(font4)

        self.gridLayout_2.addWidget(self.button6, 2, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.button_guess = QPushButton(Form)
        self.button_guess.setObjectName(u"button_guess")
        self.button_guess.setFont(font4)

        self.verticalLayout_3.addWidget(self.button_guess)

        self.verticalLayout_3.setStretch(6, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.game_label.setText(QCoreApplication.translate("Form", u"Guess the number!", None))
        self.level_label.setText(QCoreApplication.translate("Form", u"Current Difficulty: Easy", None))
        self.button_easy.setText(QCoreApplication.translate("Form", u"Easy", None))
        self.button_medium.setText(QCoreApplication.translate("Form", u"Medium", None))
        self.button_hard.setText(QCoreApplication.translate("Form", u"Hard", None))
        self.rule_label.setText(QCoreApplication.translate("Form", u"The number is between 1-100", None))
        self.button7.setText(QCoreApplication.translate("Form", u"7", None))
        self.button2.setText(QCoreApplication.translate("Form", u"2", None))
        self.button8.setText(QCoreApplication.translate("Form", u"8", None))
        self.button1.setText(QCoreApplication.translate("Form", u"1", None))
        self.button_delete.setText(QCoreApplication.translate("Form", u"Del", None))
        self.button9.setText(QCoreApplication.translate("Form", u"9", None))
        self.button4.setText(QCoreApplication.translate("Form", u"4", None))
        self.button3.setText(QCoreApplication.translate("Form", u"3", None))
        self.button_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.button5.setText(QCoreApplication.translate("Form", u"5", None))
        self.button0.setText(QCoreApplication.translate("Form", u"0", None))
        self.button6.setText(QCoreApplication.translate("Form", u"6", None))
        self.button_guess.setText(QCoreApplication.translate("Form", u"Guess", None))
    # retranslateUi

