# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospital.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HospitalMainWindow(object):
    def setupUi(self, HospitalMainWindow):
        HospitalMainWindow.setObjectName("HospitalMainWindow")
        HospitalMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HospitalMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 741, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        HospitalMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HospitalMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        HospitalMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HospitalMainWindow)
        self.statusbar.setObjectName("statusbar")
        HospitalMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HospitalMainWindow)
        QtCore.QMetaObject.connectSlotsByName(HospitalMainWindow)

    def retranslateUi(self, HospitalMainWindow):
        _translate = QtCore.QCoreApplication.translate
        HospitalMainWindow.setWindowTitle(_translate("HospitalMainWindow", "医院管理"))

