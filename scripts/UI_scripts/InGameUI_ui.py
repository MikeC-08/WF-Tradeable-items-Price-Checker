# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InGameUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QSize(1920, 1080))
        Form.setMaximumSize(QSize(1920, 1080))
        self.VoidDrop_Frame = QFrame(Form)
        self.VoidDrop_Frame.setObjectName(u"VoidDrop_Frame")
        self.VoidDrop_Frame.setGeometry(QRect(480, 610, 961, 61))
        self.VoidDrop_Frame.setFrameShape(QFrame.StyledPanel)
        self.VoidDrop_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.VoidDrop_Frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.item_2 = QLabel(self.VoidDrop_Frame)
        self.item_2.setObjectName(u"item_2")
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(18)
        self.item_2.setFont(font)

        self.gridLayout_2.addWidget(self.item_2, 2, 4, 1, 1)

        self.line_3 = QFrame(self.VoidDrop_Frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 2, 9, 2, 1)

        self.line = QFrame(self.VoidDrop_Frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 3, 2, 1)

        self.line_2 = QFrame(self.VoidDrop_Frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 2, 6, 2, 1)

        self.price_2 = QLabel(self.VoidDrop_Frame)
        self.price_2.setObjectName(u"price_2")
        self.price_2.setMinimumSize(QSize(0, 40))
        self.price_2.setFont(font)
        self.price_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.price_2, 2, 5, 1, 1)

        self.price_1 = QLabel(self.VoidDrop_Frame)
        self.price_1.setObjectName(u"price_1")
        self.price_1.setMinimumSize(QSize(0, 40))
        self.price_1.setMaximumSize(QSize(16777215, 16777215))
        self.price_1.setFont(font)
        self.price_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.price_1, 2, 2, 1, 1)

        self.item_4 = QLabel(self.VoidDrop_Frame)
        self.item_4.setObjectName(u"item_4")
        self.item_4.setFont(font)

        self.gridLayout_2.addWidget(self.item_4, 2, 10, 1, 1)

        self.item_3 = QLabel(self.VoidDrop_Frame)
        self.item_3.setObjectName(u"item_3")
        self.item_3.setFont(font)

        self.gridLayout_2.addWidget(self.item_3, 2, 7, 1, 1)

        self.item_1 = QLabel(self.VoidDrop_Frame)
        self.item_1.setObjectName(u"item_1")
        self.item_1.setFont(font)

        self.gridLayout_2.addWidget(self.item_1, 2, 1, 1, 1)

        self.price_3 = QLabel(self.VoidDrop_Frame)
        self.price_3.setObjectName(u"price_3")
        self.price_3.setMinimumSize(QSize(0, 40))
        self.price_3.setFont(font)
        self.price_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.price_3, 2, 8, 1, 1)

        self.price_4 = QLabel(self.VoidDrop_Frame)
        self.price_4.setObjectName(u"price_4")
        self.price_4.setMinimumSize(QSize(0, 40))
        self.price_4.setFont(font)
        self.price_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.price_4, 2, 11, 1, 1)

        self.Status_Holder1 = QLabel(Form)
        self.Status_Holder1.setObjectName(u"Status_Holder1")
        self.Status_Holder1.setGeometry(QRect(480, 990, 941, 20))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font1.setPointSize(12)
        self.Status_Holder1.setFont(font1)
        self.Message_holder = QLabel(Form)
        self.Message_holder.setObjectName(u"Message_holder")
        self.Message_holder.setGeometry(QRect(480, 1010, 961, 31))
        self.Message_holder.setFont(font)
        self.Message_holder.setAlignment(Qt.AlignCenter)
        self.Status_Holder = QLabel(Form)
        self.Status_Holder.setObjectName(u"Status_Holder")
        self.Status_Holder.setGeometry(QRect(480, 1041, 960, 30))
        self.Status_Holder.setMaximumSize(QSize(960, 30))
        self.Status_Holder.setFont(font1)
        self.Status_Holder.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.item_2.setText(QCoreApplication.translate("Form", u"Item-2", None))
        self.price_2.setText(QCoreApplication.translate("Form", u"-P", None))
        self.price_1.setText(QCoreApplication.translate("Form", u"-P", None))
        self.item_4.setText(QCoreApplication.translate("Form", u"Item-4", None))
        self.item_3.setText(QCoreApplication.translate("Form", u"Item-3", None))
        self.item_1.setText(QCoreApplication.translate("Form", u"Item-1", None))
        self.price_3.setText(QCoreApplication.translate("Form", u"-P", None))
        self.price_4.setText(QCoreApplication.translate("Form", u"-P", None))
        self.Status_Holder1.setText(QCoreApplication.translate("Form", u"Status Holder", None))
        self.Message_holder.setText(QCoreApplication.translate("Form", u"Message Holder", None))
        self.Status_Holder.setText(QCoreApplication.translate("Form", u"Status Holder", None))
    # retranslateUi

