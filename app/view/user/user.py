# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserMainWindow(object):
    def setupUi(self, UserMainWindow):
        UserMainWindow.setObjectName("UserMainWindow")
        UserMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        UserMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UserMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        UserMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UserMainWindow)
        self.statusbar.setObjectName("statusbar")
        UserMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UserMainWindow)

    def retranslateUi(self, UserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UserMainWindow.setWindowTitle(_translate("UserMainWindow", "产妇管理"))

