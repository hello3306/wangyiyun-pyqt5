# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, Qt

from PyQt5.QtGui import QMovie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(100, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 176, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # MainWindow.setWindowFlags(Qt.Qt.CustomizeWindowHint)

        # 设置窗体无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        # MainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)
        # 窗体透明，控件不透明
        MainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Tool)
        MainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)

        self.gif = QMovie(':/image/233.gif')
        self.label.setMovie(self.gif)
        self.gif.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    upload = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(upload)
    upload.show()
    sys.exit(app.exec_())

