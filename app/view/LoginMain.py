# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainHL.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(380, 322)
        self.centralwidget = QtWidgets.QWidget(LoginMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 80, 91, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(160, 80, 131, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        LoginMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 23))
        self.menubar.setObjectName("menubar")
        LoginMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginMainWindow)
        self.statusbar.setObjectName("statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)

    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "登录"))
        self.pushButton.setText(_translate("LoginMainWindow", "登录"))
        self.label.setText(_translate("LoginMainWindow", "用户名："))
        self.label_2.setText(_translate("LoginMainWindow", "密  码："))

