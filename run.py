"""
Create by 2019/4/26 21:13
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from app.view import LoginMain, mainWindowui
from app.config import setting


class runMainWindoe(QtWidgets.QWidget):

    def __init__(self, ui):
        self.ui = ui
        super().__init__()

    def run(self):
        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        self.user = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        if self.user == "" or self.password == "":
            try:
                self.msg()
                print(setting.API)

            except Exception as e:
                print(e)


        else:
            self.showMain()

    def msg(self):
        QMessageBox.warning(self,  # 使用infomation信息框
                            "警告",
                            "用户名或密码不能为空(＾Ｕ＾)ノ~ＹＯ",
                            QMessageBox.Yes)

    def showMain(self):
        self.Main = QMainWindow()
        self.main = mainWindowui.Ui_MainWindow()
        self.main.setupUi(self.Main)
        self.Main.show()
        print(self.user)
        self.main.label.setText(self.user)
        Form.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = LoginMain.Ui_LoginMainWindow()
    ui.setupUi(Form)
    mains = runMainWindoe(ui)
    mains.run()
    Form.show()
    sys.exit(app.exec_())
