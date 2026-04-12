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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(333, 720)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Message_holder = QLabel(Form)
        self.Message_holder.setObjectName(u"Message_holder")
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(18)
        self.Message_holder.setFont(font)

        self.gridLayout.addWidget(self.Message_holder, 0, 0, 1, 2)

        self.price_4 = QLabel(Form)
        self.price_4.setObjectName(u"price_4")
        self.price_4.setMinimumSize(QSize(0, 40))
        self.price_4.setFont(font)
        self.price_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.price_4, 11, 1, 1, 1)

        self.price_3 = QLabel(Form)
        self.price_3.setObjectName(u"price_3")
        self.price_3.setMinimumSize(QSize(0, 40))
        self.price_3.setFont(font)
        self.price_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.price_3, 9, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font1.setPointSize(26)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.Title = QLabel(Form)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(0, 40))
        self.Title.setFont(font1)
        self.Title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Title, 2, 0, 1, 1)

        self.item_1 = QLabel(Form)
        self.item_1.setObjectName(u"item_1")
        self.item_1.setFont(font)

        self.gridLayout.addWidget(self.item_1, 3, 0, 1, 1)

        self.price_1 = QLabel(Form)
        self.price_1.setObjectName(u"price_1")
        self.price_1.setMinimumSize(QSize(0, 40))
        self.price_1.setMaximumSize(QSize(16777215, 16777215))
        self.price_1.setFont(font)
        self.price_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.price_1, 3, 1, 1, 1)

        self.item_2 = QLabel(Form)
        self.item_2.setObjectName(u"item_2")
        self.item_2.setFont(font)

        self.gridLayout.addWidget(self.item_2, 7, 0, 1, 1)

        self.price_2 = QLabel(Form)
        self.price_2.setObjectName(u"price_2")
        self.price_2.setMinimumSize(QSize(0, 40))
        self.price_2.setFont(font)
        self.price_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.price_2, 7, 1, 1, 1)

        self.item_3 = QLabel(Form)
        self.item_3.setObjectName(u"item_3")
        self.item_3.setFont(font)

        self.gridLayout.addWidget(self.item_3, 9, 0, 1, 1)

        self.item_4 = QLabel(Form)
        self.item_4.setObjectName(u"item_4")
        self.item_4.setFont(font)

        self.gridLayout.addWidget(self.item_4, 11, 0, 1, 1)

        self.Status_Holder = QLabel(Form)
        self.Status_Holder.setObjectName(u"Status_Holder")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font2.setPointSize(12)
        self.Status_Holder.setFont(font2)

        self.gridLayout.addWidget(self.Status_Holder, 1, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Message_holder.setText("")
        self.price_4.setText(QCoreApplication.translate("Form", u"-P", None))
        self.price_3.setText(QCoreApplication.translate("Form", u"-P", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u50f9\u683c", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u540d\u7a31", None))
        self.item_1.setText(QCoreApplication.translate("Form", u"Item-1", None))
        self.price_1.setText(QCoreApplication.translate("Form", u"-P", None))
        self.item_2.setText(QCoreApplication.translate("Form", u"Item-2", None))
        self.price_2.setText(QCoreApplication.translate("Form", u"-P", None))
        self.item_3.setText(QCoreApplication.translate("Form", u"Item-3", None))
        self.item_4.setText(QCoreApplication.translate("Form", u"Item-4", None))
        self.Status_Holder.setText("")
    # retranslateUi

