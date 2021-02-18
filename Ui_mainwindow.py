# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Display_Brws = QTextBrowser(self.centralwidget)
        self.Display_Brws.setObjectName(u"Display_Brws")

        self.gridLayout.addWidget(self.Display_Brws, 0, 0, 1, 2)

        self.Start_PB = QPushButton(self.centralwidget)
        self.Start_PB.setObjectName(u"Start_PB")

        self.gridLayout.addWidget(self.Start_PB, 1, 0, 1, 1)

        self.Stop_PB = QPushButton(self.centralwidget)
        self.Stop_PB.setObjectName(u"Stop_PB")

        self.gridLayout.addWidget(self.Stop_PB, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Start_PB.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Stop_PB.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

