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
        MainWindow.resize(1121, 971)
        MainWindow.setStyleSheet("background:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 150, 1101, 751))
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
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_21.addWidget(self.label_17)
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
        self.verticalLayout_21.addWidget(self.pushButton_12)
        self.horizontalLayout.addLayout(self.verticalLayout_21)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_20.addWidget(self.label_18)
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
        self.verticalLayout_20.addWidget(self.pushButton_11)
        self.horizontalLayout.addLayout(self.verticalLayout_20)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_22.addWidget(self.label_19)
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
        self.verticalLayout_22.addWidget(self.pushButton_13)
        self.horizontalLayout.addLayout(self.verticalLayout_22)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_18.addWidget(self.label_20)
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
        self.verticalLayout_18.addWidget(self.pushButton_9)
        self.horizontalLayout.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_19.addWidget(self.label_21)
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
        self.verticalLayout_19.addWidget(self.pushButton_10)
        self.horizontalLayout.addLayout(self.verticalLayout_19)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_23.addWidget(self.label_22)
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
        self.verticalLayout_23.addWidget(self.pushButton_14)
        self.horizontalLayout.addLayout(self.verticalLayout_23)
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
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1091, 721))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_11.addWidget(self.pushButton_16)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_12.addWidget(self.pushButton_17)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_13.addWidget(self.label_12)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_13.addWidget(self.pushButton_18)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_14.addWidget(self.label_13)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_14.addWidget(self.pushButton_19)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_15.addWidget(self.label_14)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_15.addWidget(self.pushButton_20)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_16.addWidget(self.label_15)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_16.addWidget(self.pushButton_21)
        self.horizontalLayout_3.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setStyleSheet("font: 17pt \"微软雅黑\";\n"
"")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_17.addWidget(self.label_16)
        self.pushButton_22 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 71))
        self.pushButton_22.setStyleSheet("\n"
"text-align : center;\n"
"background-color : rgb(0,193,222);\n"
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
        self.verticalLayout_17.addWidget(self.pushButton_22)
        self.horizontalLayout_3.addLayout(self.verticalLayout_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem4)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget_3.setStyleSheet("")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_11)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_11)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setStyleSheet("\n"
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
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.pushButton_25 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_25.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_25.setStyleSheet("\n"
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
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_7.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_26.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_26.setStyleSheet("\n"
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
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_7.addWidget(self.pushButton_26)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_12)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(14)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(13, item)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_12)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setStyleSheet("\n"
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
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.pushButton_23 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_23.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_23.setStyleSheet("\n"
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
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_6.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_24.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_24.setStyleSheet("\n"
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
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_6.addWidget(self.pushButton_24)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_13)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(14)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, item)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_13)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_4.setStyleSheet("\n"
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
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_8.addWidget(self.lineEdit_4)
        self.pushButton_27 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_27.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_27.setStyleSheet("\n"
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
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_8.addWidget(self.pushButton_27)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_14)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(14)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(13, item)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_14)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_5.setStyleSheet("\n"
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
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_9.addWidget(self.lineEdit_5)
        self.pushButton_29 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_29.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_29.setStyleSheet("\n"
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
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_9.addWidget(self.pushButton_29)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_15)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(14)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(13, item)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_15)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_6.setStyleSheet("\n"
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
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_10.addWidget(self.lineEdit_6)
        self.pushButton_31 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_31.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_31.setStyleSheet("\n"
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
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_10.addWidget(self.pushButton_31)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_16)
        self.tableWidget_7.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(14)
        self.tableWidget_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(13, item)
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab_16)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.lineEdit_7.setStyleSheet("\n"
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
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_11.addWidget(self.lineEdit_7)
        self.pushButton_33 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_33.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_33.setStyleSheet("\n"
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
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_11.addWidget(self.pushButton_33)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_17)
        self.tableWidget_8.setGeometry(QtCore.QRect(0, 60, 1081, 491))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(8)
        self.tableWidget_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(7, item)
        self.layoutWidget_7 = QtWidgets.QWidget(self.tab_17)
        self.layoutWidget_7.setGeometry(QtCore.QRect(0, 10, 1081, 41))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_8.setStyleSheet("\n"
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
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_12.addWidget(self.lineEdit_8)
        self.pushButton_35 = QtWidgets.QPushButton(self.layoutWidget_7)
        self.pushButton_35.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_35.setStyleSheet("\n"
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
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_12.addWidget(self.pushButton_35)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.tabWidget_3.addTab(self.tab_17, "")
        self.verticalLayout_3.addWidget(self.tabWidget_3)
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
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 241, 41))
        self.label_9.setStyleSheet("image: url(:/image/国家健康医疗大数据展示平台.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 1101, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 61))
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
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setStyleSheet("text-align : center;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_7.addWidget(self.pushButton_5)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setStyleSheet("text-align : center;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_8.addWidget(self.pushButton_6)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_9.addWidget(self.pushButton_7)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 61))
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
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
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
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "宝宝云平台"))
        self.label_17.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "制作中"))
        self.label_18.setText(_translate("MainWindow", " 0"))
        self.pushButton_11.setText(_translate("MainWindow", "待制作"))
        self.label_19.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "待审核"))
        self.label_20.setText(_translate("MainWindow", "0"))
        self.pushButton_9.setText(_translate("MainWindow", "待完善"))
        self.label_21.setText(_translate("MainWindow", "0"))
        self.pushButton_10.setText(_translate("MainWindow", "已完善"))
        self.label_22.setText(_translate("MainWindow", "0"))
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
        self.label_10.setText(_translate("MainWindow", "0"))
        self.pushButton_16.setText(_translate("MainWindow", "待安装"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.pushButton_17.setText(_translate("MainWindow", "已安装"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.pushButton_18.setText(_translate("MainWindow", "待检测"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.pushButton_19.setText(_translate("MainWindow", "已检测"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.pushButton_20.setText(_translate("MainWindow", "待入库"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.pushButton_21.setText(_translate("MainWindow", "已入库"))
        self.label_16.setText(_translate("MainWindow", "0"))
        self.pushButton_22.setText(_translate("MainWindow", "已领用"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "产品名称"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "规格"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "单位"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "剩余数量"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "备注"))
        self.pushButton_25.setText(_translate("MainWindow", "搜索"))
        self.pushButton_26.setText(_translate("MainWindow", "添加材料"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "待安装"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备状态"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "提交"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "设备ID"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "设备颜色"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "设备版本"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "螺丝是否完整"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "镜头盖是否盖上"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "设备是否安装内存卡"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "内存卡是否格式化"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "摄像头是否校准"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "设备是否正常"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "入库人"))
        item = self.tableWidget_3.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "入库日期"))
        self.pushButton_23.setText(_translate("MainWindow", "搜索"))
        self.pushButton_24.setText(_translate("MainWindow", "添加设备"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "已安装"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备状态"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "提交"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "设备ID"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "设备颜色"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "设备版本"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "螺丝是否完整"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "镜头盖是否盖上"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "设备是否安装内存卡"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "内存卡是否格式化"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "摄像头是否校准"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "设备是否正常"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "入库人"))
        item = self.tableWidget_4.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "入库日期"))
        self.pushButton_27.setText(_translate("MainWindow", "搜索"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "待检测"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备状态"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "提交"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "设备ID"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "设备颜色"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "设备版本"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "螺丝是否完整"))
        item = self.tableWidget_5.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "镜头盖是否盖上"))
        item = self.tableWidget_5.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "设备是否安装内存卡"))
        item = self.tableWidget_5.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "内存卡是否格式化"))
        item = self.tableWidget_5.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "摄像头是否校准"))
        item = self.tableWidget_5.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "设备是否正常"))
        item = self.tableWidget_5.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "入库人"))
        item = self.tableWidget_5.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "入库日期"))
        self.pushButton_29.setText(_translate("MainWindow", "搜索"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MainWindow", "已检测"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备状态"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "提交"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "设备ID"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "设备颜色"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "设备版本"))
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "螺丝是否完整"))
        item = self.tableWidget_6.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "镜头盖是否盖上"))
        item = self.tableWidget_6.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "设备是否安装内存卡"))
        item = self.tableWidget_6.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "内存卡是否格式化"))
        item = self.tableWidget_6.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "摄像头是否校准"))
        item = self.tableWidget_6.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "设备是否正常"))
        item = self.tableWidget_6.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "入库人"))
        item = self.tableWidget_6.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "入库日期"))
        self.pushButton_31.setText(_translate("MainWindow", "搜索"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MainWindow", "待入库"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备状态"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "提交"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "设备ID"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "设备颜色"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "设备版本"))
        item = self.tableWidget_7.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "螺丝是否完整"))
        item = self.tableWidget_7.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "镜头盖是否盖上"))
        item = self.tableWidget_7.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "设备是否安装内存卡"))
        item = self.tableWidget_7.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "内存卡是否格式化"))
        item = self.tableWidget_7.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "摄像头是否校准"))
        item = self.tableWidget_7.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "设备是否正常"))
        item = self.tableWidget_7.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "入库人"))
        item = self.tableWidget_7.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "入库日期"))
        self.pushButton_33.setText(_translate("MainWindow", "搜索"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MainWindow", "已入库"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备ID"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "设备颜色"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "设备版本"))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "入库日期"))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "领用人"))
        item = self.tableWidget_8.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "领取日期"))
        item = self.tableWidget_8.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "领用医院"))
        self.pushButton_35.setText(_translate("MainWindow", "搜索"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), _translate("MainWindow", "已领用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "设备管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "二维码管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "消息管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "信息管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "订单管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "素材下载"))
        self.label.setText(_translate("MainWindow", "产妇管理"))
        self.label_2.setText(_translate("MainWindow", "医院管理"))
        self.label_3.setText(_translate("MainWindow", "设备管理"))
        self.label_4.setText(_translate("MainWindow", "二维码管理"))
        self.label_5.setText(_translate("MainWindow", "消息管理"))
        self.label_6.setText(_translate("MainWindow", "信息管理"))
        self.label_7.setText(_translate("MainWindow", "订单管理"))
        self.label_8.setText(_translate("MainWindow", "素材下载"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "版本信息"))


