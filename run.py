"""
Create by 2019/4/26 21:13
"""
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


from app.model.hospital import hospitalModel
from app.view.hospital import hospital
from app.view.login import LoginMain
from app.view.main import mainWindowui
from app.view.user import user


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
                QMessageBox.warning(self,  # 使用infomation信息框
                                    "警告",
                                    "用户名或密码不能为空(＾Ｕ＾)ノ~ＹＯ",
                                    QMessageBox.Yes)
            except Exception as e:
                print(e)


        else:
            self.showMain()

    # 显示主页
    def showMain(self):
        self.Main = QMainWindow()
        self.main = mainWindowui.Ui_MainWindow()
        self.main.setupUi(self.Main)
        self.Main.show()

        # 按钮点击事件
        self.main.pushButton.clicked.connect(self.showUser)
        self.main.pushButton_2.clicked.connect(self.showHospital)

        Form.close()

    # 产妇管理
    def showUser(self):
        self.UserMain = QMainWindow()
        self.user = user.Ui_UserMainWindow()
        self.user.setupUi(self.UserMain)
        self.UserMain.show()

    # 医院管理
    def showHospital(self):
        self.HospitalMain = QMainWindow()
        self.hospital = hospital.Ui_HospitalMainWindow()
        self.hospital.setupUi(self.HospitalMain)
        self.HospitalMain.show()
        hModel = hospitalModel(self.hospital)
        hModel.run()


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
