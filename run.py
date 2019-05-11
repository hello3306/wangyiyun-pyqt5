"""
Create by 2019/4/26 21:13
"""
import json
import time

from app.model.user import userModel
from image.img import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cacheout import Cache
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from app.model.login import loginModel

from app.config.setting import *

from app.server.login import Login as LoginServer
from app.view.login import LoginMain
from app.view.main import mainWindowui
from app.model.main import mainModel


class runMainWindoe(QtWidgets.QWidget):

    def __init__(self, ui):
        self.ui = ui
        super().__init__()
        self.cache = Cache(maxsize=MAXSIZE, ttl=TTL, timer=time.time)

    def run(self):
        # 实例化登录model
        login = loginModel(ui)
        login.run()

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.onButtonClick)

    # 关闭登录窗口
    def onButtonClick(self):
        qApp = QApplication.instance()
        qApp.quit()

    # 登录
    def login(self):
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
                # 用户勾选保存密码
                if self.ui.checkBox.isChecked():
                    self.save_login_info(self.user, self.password)

                # 显示主页面
                self.showMain()

                # 保存token在缓存里面
                data = json.loads(res.text)
                self.cache.set('token', data['token'])
            else:
                QMessageBox.warning(self,  # 使用infomation信息框
                                    "警告",
                                    "用户名或密码错误(＾Ｕ＾)ノ~ＹＯ",
                                    QMessageBox.Yes)

    def save_login_info(self, user, password):
        self.setting = QSettings("config.ini", QSettings.IniFormat)
        self.setting.setValue("user", user)
        self.setting.setValue("password", password)

    # 显示主页
    def showMain(self):
        self.Main = QMainWindow()
        self.main = mainWindowui.Ui_MainWindow()
        self.main.setupUi(self.Main)

        # mainM = mainModel(self.main)
        # mainM.run()

        # 设置窗体图标
        self.Main.setWindowIcon(QIcon(':/image/大数据1.png'))
        # 禁止窗口最大化
        self.Main.setFixedSize(self.Main.width(), self.Main.height())
        # 设置窗体左下角文本信息
        self.Main.statusBar().showMessage("当前用户：超级管理员")
        # 主页面按钮点击事件
        self.pushButtons()

        self.Main.show()
        # self.showUser()

        Form.close()

    def pushButtons(self):
        # 顶部按钮点击事件
        self.main.pushButton.clicked.connect(self.showUser)
        self.main.pushButton_2.clicked.connect(self.showHospital)
        self.main.pushButton_3.clicked.connect(self.showEquipment)
        self.main.pushButton_4.clicked.connect(self.showCord)
        self.main.pushButton_5.clicked.connect(self.showMsg)
        self.main.pushButton_6.clicked.connect(self.showInformation)
        self.main.pushButton_7.clicked.connect(self.showOrder)
        self.main.pushButton_8.clicked.connect(self.showMaterial)
        self.main.pushButton_15.clicked.connect(self.searh)

        #   设备管理按钮点击事件
        self.main.pushButton_16.clicked.connect(self.showSheibei0)
        self.main.pushButton_17.clicked.connect(self.showSheibei1)
        self.main.pushButton_18.clicked.connect(self.showSheibei2)
        self.main.pushButton_19.clicked.connect(self.showSheibei3)
        self.main.pushButton_20.clicked.connect(self.showSheibei4)
        self.main.pushButton_21.clicked.connect(self.showSheibei5)
        self.main.pushButton_22.clicked.connect(self.showSheibei6)

    # 查询
    def searh(self):
        text = self.main.lineEdit.text()
        print(text)

    # 产妇管理
    def showUser(self):
        # from app.model.user import userModel
        self.main.tabWidget.setCurrentIndex(0)
        # user = User(self.cache)
        # res = user.getUserInfo()
        # if res.status_code == 200:
        #     data = json.loads(res.text)
        UserModel = userModel(self.main, self.cache)
        UserModel.run()
        # print(data['data'])

        # else:
        #     print("请求失败")
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

    def showSheibei0(self):
        self.main.tabWidget_3.setCurrentIndex(0)

    def showSheibei1(self):
        self.main.tabWidget_3.setCurrentIndex(1)

    def showSheibei2(self):
        self.main.tabWidget_3.setCurrentIndex(2)

    def showSheibei3(self):
        self.main.tabWidget_3.setCurrentIndex(3)

    def showSheibei4(self):
        self.main.tabWidget_3.setCurrentIndex(4)

    def showSheibei5(self):
        self.main.tabWidget_3.setCurrentIndex(5)

    def showSheibei6(self):
        self.main.tabWidget_3.setCurrentIndex(6)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = LoginMain.Ui_LoginMainWindow()
    ui.setupUi(Form)
    mains = runMainWindoe(ui)
    mains.run()
    # 设置登录框的图标
    Form.setWindowIcon(QIcon(':/image/大数据1.png'))
    # 禁止最大化
    Form.setFixedSize(Form.width(), Form.height())
    # 隐藏窗口边框
    Form.setWindowFlags(Qt.Qt.CustomizeWindowHint)

    Form.show()
    sys.exit(app.exec_())
