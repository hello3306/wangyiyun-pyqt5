# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginMain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication

from image.img import *
from PyQt5.QtGui import QMovie


class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(414, 298)
        LoginMainWindow.setStyleSheet("background:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(LoginMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 235, 37))
        self.pushButton.setMinimumSize(QtCore.QSize(235, 37))
        self.pushButton.setStyleSheet("\n"
                                      "text-align : center;\n"
                                      "background-color : rgb(7,189,253);\n"
                                      "font: bold;\n"
                                      "border-color: gray; \n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 6px;\n"
                                      "height : 14px;\n"
                                      "border-style: outset;\n"
                                      "font : 14px;}\n"
                                      "QPushButton:pressed\n"
                                      "{text-align : center;\n"
                                      "background-color : light gray;\n"
                                      "font: bold;\n"
                                      "border-color: gray;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 6px;\n"
                                      "height : 14px;\n"
                                      "border-style: outset;\n"
                                      "font : 14px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 91, 71))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(113, 101, 231, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setStyleSheet("text-align : center;\n"
                                    "background-color : white;\n"
                                    "font: bold;\n"
                                    "border-color: gray; \n"
                                    "border-width: 2px;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 6px;\n"
                                    "height : 14px;\n"
                                    "border-style: outset;\n"
                                    "font : 14px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setStyleSheet("text-align : center;\n"
                                      "background-color : white;\n"
                                      "font: bold;\n"
                                      "border-color: gray; \n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 6px;\n"
                                      "height : 14px;\n"
                                      "border-style: outset;\n"
                                      "font : 14px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 110, 31, 31))
        self.label.setMinimumSize(QtCore.QSize(24, 24))
        self.label.setMaximumSize(QtCore.QSize(48, 48))
        self.label.setStyleSheet("border-image: url(:/image/用户.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 31, 31))
        self.label_2.setMaximumSize(QtCore.QSize(48, 48))
        self.label_2.setStyleSheet("border-image: url(:/image/密码.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 0, 21, 21))
        self.pushButton_2.setStyleSheet("border-image: url(:/image/关闭.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        LoginMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 23))
        self.menubar.setObjectName("menubar")
        LoginMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginMainWindow)
        self.statusbar.setObjectName("statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        # 禁止最大化
        LoginMainWindow.setFixedSize(LoginMainWindow.width(), LoginMainWindow.height())
        # 隐藏窗口边框
        LoginMainWindow.setWindowFlags(Qt.Qt.CustomizeWindowHint)

        self.gif = QMovie(':/image/111.gif')
        self.label_3.setMovie(self.gif)
        self.gif.start()

        self.pushButton_2.clicked.connect(self.onButtonClick)

        self.retranslateUi(LoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)

    #
    def onButtonClick(self):
        # sender 是发送信号的对象，此处发送信号的对象是button1按钮
        qApp = QApplication.instance()
        qApp.quit()

    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("LoginMainWindow", "登录"))
