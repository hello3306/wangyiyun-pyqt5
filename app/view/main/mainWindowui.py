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
        MainWindow.resize(1158, 958)
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
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
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
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(120, 30, 1001, 881))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_9.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(182, 179, 179);\n"
"font: bold;\n"
"color:white;\n"
"border-color: gray; \n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"height : 14px;\n"
"border-style: outset;\n"
"font : 14px;}\n"
"QPushButton:pressed\n"
"{text-align : center;\n"
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setMinimumSize(QtCore.QSize(99, 71))
        self.pushButton_10.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(218, 84, 46);\n"
"font: bold;\n"
"color:white;\n"
"border-color: gray; \n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"height : 14px;\n"
"border-style: outset;\n"
"font : 14px;}\n"
"QPushButton:pressed\n"
"{text-align : center;\n"
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setMinimumSize(QtCore.QSize(99, 71))
        self.pushButton_11.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(255,184,72);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setMinimumSize(QtCore.QSize(129, 71))
        self.pushButton_12.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(34,84,164);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setMinimumSize(QtCore.QSize(99, 71))
        self.pushButton_13.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(39,169,227);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setMinimumSize(QtCore.QSize(99, 71))
        self.pushButton_14.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(40,183,121);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setStyleSheet("\n"
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
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_15.setStyleSheet("\n"
"\n"
"text-align : center;\n"
"background-color : rgb(0, 193, 222);\n"
"font: bold;\n"
"color:white;\n"
"border-color: gray; \n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"height : 14px;\n"
"border-style: outset;\n"
"font : 14px;}\n"
"QPushButton:pressed\n"
"{text-align : center;\n"
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_2.addWidget(self.pushButton_15)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 20, 1001, 841))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.widget = QtWidgets.QWidget(self.tab_9)
        self.widget.setGeometry(QtCore.QRect(0, -10, 991, 801))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_16.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(182, 179, 179);\n"
"font: bold;\n"
"color:white;\n"
"border-color: gray; \n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"height : 14px;\n"
"border-style: outset;\n"
"font : 14px;}\n"
"QPushButton:pressed\n"
"{text-align : center;\n"
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_3.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_17.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(218, 84, 46);\n"
"font: bold;\n"
"color:white;\n"
"border-color: gray; \n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"height : 14px;\n"
"border-style: outset;\n"
"font : 14px;}\n"
"QPushButton:pressed\n"
"{text-align : center;\n"
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_18.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(255,184,72);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_19.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(34,84,164);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_3.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.widget)
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_20.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(39,169,227);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_3.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.widget)
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_21.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(40,183,121);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_3.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.widget)
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_22.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(40,183,121);\n"
"color:white;\n"
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
"background-color :rgb(0,0,0);\n"
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
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_3.addWidget(self.pushButton_22)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem5)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_3.setStyleSheet("background-img:url(:/image/shebei.png)")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tabWidget_3.addTab(self.tab_17, "")
        self.verticalLayout_3.addWidget(self.tabWidget_3)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_3.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
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
        self.pushButton_9.setText(_translate("MainWindow", "待完善"))
        self.pushButton_10.setText(_translate("MainWindow", "已完善"))
        self.pushButton_11.setText(_translate("MainWindow", "待制作"))
        self.pushButton_12.setText(_translate("MainWindow", "制作中"))
        self.pushButton_13.setText(_translate("MainWindow", "待审核"))
        self.pushButton_14.setText(_translate("MainWindow", "已发布"))
        self.pushButton_15.setText(_translate("MainWindow", "搜索"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "产妇名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "手机号码"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "所属医院"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "预产期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "建档时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "产妇信息"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "提交"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "重置密码"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "是否停用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "产妇管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "医院管理"))
        self.pushButton_16.setText(_translate("MainWindow", "待安装"))
        self.pushButton_17.setText(_translate("MainWindow", "已安装"))
        self.pushButton_18.setText(_translate("MainWindow", "待检测"))
        self.pushButton_19.setText(_translate("MainWindow", "已检测"))
        self.pushButton_20.setText(_translate("MainWindow", "待入库"))
        self.pushButton_21.setText(_translate("MainWindow", "已入库"))
        self.pushButton_22.setText(_translate("MainWindow", "已领用"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "待安装"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "已安装"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "待检测"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MainWindow", "已检测"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MainWindow", "待入库"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MainWindow", "已入库"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), _translate("MainWindow", "已领用"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "设备装机"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "设备管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "设备管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "二维码管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "消息管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "信息管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "订单管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "素材下载"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "版本信息"))

from image.img import *
