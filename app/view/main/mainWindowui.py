# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 584)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 130, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 130, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 130, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 280, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 280, 54, 12))
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 711, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton.setMaximumSize(QtCore.QSize(226, 16777215))
        self.pushButton.setStyleSheet("\n"
"text-align : center;\n"
"background-color : white;\n"
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
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_2.setStyleSheet("text-align : center;\n"
"background-color : white;\n"
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
"")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/医院.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_3.setStyleSheet("text-align : center;\n"
"background-color : white;\n"
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
"")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/设备.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_4.setStyleSheet("text-align : center;\n"
"background-color : white;\n"
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
"")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/二维码.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 150, 711, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_5.setStyleSheet("\n"
"text-align : center;\n"
"background-color : white;\n"
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
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/消息.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_6.setStyleSheet("\n"
"text-align : center;\n"
"background-color : white;\n"
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
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/新闻.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_7.setStyleSheet("\n"
"text-align : center;\n"
"background-color : white;\n"
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
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/订 单.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 91))
        self.pushButton_8.setStyleSheet("\n"
"text-align : center;\n"
"background-color : white;\n"
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
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/素材库.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 280, 54, 12))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "宝宝云平台"))
        self.label.setText(_translate("MainWindow", "产妇管理"))
        self.label_2.setText(_translate("MainWindow", "医院管理"))
        self.label_3.setText(_translate("MainWindow", "设备管理"))
        self.label_4.setText(_translate("MainWindow", "二维码管理"))
        self.label_5.setText(_translate("MainWindow", "消息管理"))
        self.label_6.setText(_translate("MainWindow", "信息管理"))
        self.label_7.setText(_translate("MainWindow", "订单管理"))
        self.label_8.setText(_translate("MainWindow", "素材下载"))

