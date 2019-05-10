"""
 Hello 

"""
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication


class loginModel(QtWidgets.QWidget):

    def __init__(self, ui):
        self.ui = ui

    def run(self):
        self.ui.gif = QMovie(':/image/111.gif')
        self.ui.label_3.setMovie(self.ui.gif)
        self.ui.gif.start()
        # self.ui.pushButton_2.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        qApp = QApplication.instance()
        qApp.quit()
