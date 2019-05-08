"""
Create by 2019/4/26 21:13
"""
import json
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cacheout import Cache

from app.view.login import LoginMain
from app.view.main import mainWindowui
from app.server.login import Login as LoginServer
from app.config.setting import *


class runMainWindoe(QtWidgets.QWidget):

    def __init__(self, ui):
        self.ui = ui
        super().__init__()
        self.cache = Cache(maxsize=MAXSIZE, ttl=TTL, timer=time.time)

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
            loginserver = LoginServer(self.user, self.password)
            res = loginserver.run()
            if res.status_code == 200:
                self.showMain()
                data = json.loads(res.text)
                print(data)
                self.cache.set('token', data['token'])
            else:
                QMessageBox.warning(self,  # 使用infomation信息框
                                    "警告",
                                    "用户名或密码错误(＾Ｕ＾)ノ~ＹＯ",
                                    QMessageBox.Yes)

    # 显示主页
    def showMain(self):
        self.Main = QMainWindow()
        self.main = mainWindowui.Ui_MainWindow()
        self.main.setupUi(self.Main)
        self.Main.show()

        # 按钮点击事件
        self.main.pushButton.clicked.connect(self.showUser)
        self.main.pushButton_2.clicked.connect(self.showHospital)
        self.main.pushButton_3.clicked.connect(self.showEquipment)
        self.main.pushButton_4.clicked.connect(self.showCord)
        self.main.pushButton_5.clicked.connect(self.showMsg)
        self.main.pushButton_6.clicked.connect(self.showInformation)
        self.main.pushButton_7.clicked.connect(self.showOrder)
        self.main.pushButton_8.clicked.connect(self.showMaterial)

        Form.close()

    # 产妇管理
    def showUser(self):
        self.main.tabWidget.setCurrentIndex(0)
        print(self.cache.get('token'))
        # self.UserMain = QMainWindow()
        # self.user = user.Ui_UserMainWindow()
        # self.user.setupUi(self.UserMain)
        # self.UserMain.show()

    # 医院管理
    def showHospital(self):
        self.main.tabWidget.setCurrentIndex(1)
        # self.HospitalMain = QMainWindow()
        # self.hospital = hospital.Ui_HospitalMainWindow()
        # self.hospital.setupUi(self.HospitalMain)
        # self.HospitalMain.show()
        # hModel = hospitalModel(self.hospital)
        # hModel.run()

    # 设备管理
    def showEquipment(self):
        self.main.tabWidget.setCurrentIndex(2)

    # 二维码管理
    def showCord(self):
        self.main.tabWidget.setCurrentIndex(3)

    # 消息管理
    def showMsg(self):
        self.main.tabWidget.setCurrentIndex(4)

    # 信息管理
    def showInformation(self):
        self.main.tabWidget.setCurrentIndex(5)

    # 订单管理
    def showOrder(self):
        self.main.tabWidget.setCurrentIndex(6)

    # 素材下载
    def showMaterial(self):
        self.main.tabWidget.setCurrentIndex(7)


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
