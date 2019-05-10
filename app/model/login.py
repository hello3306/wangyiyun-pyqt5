"""
 Hello 

"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QMovie


class loginModel(QtWidgets.QWidget):

    def __init__(self, ui):
        self.ui = ui

    def run(self):
        self.ui.gif = QMovie(':/image/111.gif')
        self.ui.label_3.setMovie(self.ui.gif)
        self.ui.gif.start()
        settings = QSettings("config.ini", QSettings.IniFormat)
        if settings.value("user") and settings.value("password"):
            self.ui.lineEdit.setText(settings.value("user"))
            self.ui.lineEdit_2.setText(settings.value("password"))
            self.ui.checkBox.setChecked(True)

        # check = self.ui.checkBox.isChecked()
        # print(check)
