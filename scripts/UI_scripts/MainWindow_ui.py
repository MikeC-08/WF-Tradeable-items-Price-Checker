# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 341)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.Start_btn = QPushButton(self.centralwidget)
        self.Start_btn.setObjectName(u"Start_btn")
        self.Start_btn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(20)
        self.Start_btn.setFont(font)

        self.gridLayout.addWidget(self.Start_btn, 3, 1, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 0, 1, 7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 1)

        self.no_of_people_Dropdown = QComboBox(self.centralwidget)
        self.no_of_people_Dropdown.addItem("")
        self.no_of_people_Dropdown.addItem("")
        self.no_of_people_Dropdown.addItem("")
        self.no_of_people_Dropdown.addItem("")
        self.no_of_people_Dropdown.setObjectName(u"no_of_people_Dropdown")
        self.no_of_people_Dropdown.setMinimumSize(QSize(0, 27))
        self.no_of_people_Dropdown.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.no_of_people_Dropdown, 1, 4, 1, 1)

        self.Tips = QLabel(self.centralwidget)
        self.Tips.setObjectName(u"Tips")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font1.setPointSize(12)
        self.Tips.setFont(font1)
        self.Tips.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Tips, 2, 1, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 6, 1, 1)

        self.Stop_btn = QPushButton(self.centralwidget)
        self.Stop_btn.setObjectName(u"Stop_btn")
        self.Stop_btn.setMinimumSize(QSize(257, 0))
        self.Stop_btn.setFont(font)

        self.gridLayout.addWidget(self.Stop_btn, 5, 1, 1, 5)

        self.no_of_people_label = QLabel(self.centralwidget)
        self.no_of_people_label.setObjectName(u"no_of_people_label")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font2.setPointSize(18)
        self.no_of_people_label.setFont(font2)
        self.no_of_people_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.no_of_people_label, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 492, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Start_btn.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.no_of_people_Dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.no_of_people_Dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.no_of_people_Dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.no_of_people_Dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"1", None))

        self.Tips.setText(QCoreApplication.translate("MainWindow", u"\u6309\u4e0b\"Enter\"\u6383\u63cf, \u518d\u6309\u7d50\u675f", None))
        self.Stop_btn.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.no_of_people_label.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u6578", None))
    # retranslateUi

