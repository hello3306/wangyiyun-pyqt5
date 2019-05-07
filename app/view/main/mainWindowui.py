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
        MainWindow.resize(1142, 963)
        MainWindow.setStyleSheet("background:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 91, 891))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 51))
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
        icon.addPixmap(QtGui.QPixmap(":/image/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("text-align : center;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 51))
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
        icon1.addPixmap(QtGui.QPixmap(":/image/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 51))
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
        icon2.addPixmap(QtGui.QPixmap(":/image/shebei.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 51))
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
        icon3.addPixmap(QtGui.QPixmap(":/image/qr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 51))
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
        icon4.addPixmap(QtGui.QPixmap(":/image/msg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 51))
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
        icon5.addPixmap(QtGui.QPixmap(":/image/dingdang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 51))
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
        icon6.addPixmap(QtGui.QPixmap(":/image/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 51))
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
        icon7.addPixmap(QtGui.QPixmap(":/image/sucaiku.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(120, 20, 1011, 891))
        self.tableView.setStyleSheet("background:url(:/image/hospital.png);\n"
                                     "background:rgb(227, 227, 227)")
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 23))
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
        self.label.setText(_translate("MainWindow", "  产妇管理"))
        self.label_2.setText(_translate("MainWindow", "  医院管理"))
        self.label_3.setText(_translate("MainWindow", "  设备管理"))
        self.label_4.setText(_translate("MainWindow", "  二维码管理"))
        self.label_5.setText(_translate("MainWindow", "  消息管理"))
        self.label_6.setText(_translate("MainWindow", "  信息管理"))
        self.label_7.setText(_translate("MainWindow", "  订单管理"))
        self.label_8.setText(_translate("MainWindow", "  素材下载"))


from image.img import *
