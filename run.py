"""
Create by 2019/4/26 21:13
"""
import json
import time

from image.img import *
from app.model.user import userModel
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSystemTrayIcon, QMenu, QAction
from cacheout import Cache
from PyQt5 import QtWidgets, Qt
from app.model.login import loginModel
from app.config.setting import *
from app.server.login import Login as LoginServer
from app.view.login import LoginMain
from app.view.main import mainWindowui
from app.model.addMaterial import addMaterial as MaterialModel
from app.view.add_material import new_material as newMaterialView
from app.model.newMaterial import newMaterial as newMaterialModel
from app.view.add_material import add_material
from app.view.add_shebei import add_equipment


class runMainWindoe(QtWidgets.QWidget, QSystemTrayIcon):

    def __init__(self, ui):
        self.ui = ui
        super(runMainWindoe, self).__init__()
        self.cache = Cache(maxsize=MAXSIZE, ttl=TTL, timer=time.time)

    def run(self):
        # 实例化登录model
        login = loginModel(ui)
        login.run()

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.onButtonClick)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '警告', '退出后测试将停止,\n你确认要退出吗？',
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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

    # 保存登录信息
    def save_login_info(self, user, password):
        self.setting = QSettings("config.ini", QSettings.IniFormat)
        self.setting.setValue("user", user)
        self.setting.setValue("password", password)

    # 显示主页
    def showMain(self):
        self.Tary()
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

    # 右下角程序图标
    def Tary(self):
        self.tray = QSystemTrayIcon()

        # 设置程序任务栏图标
        self.tray.setIcon(QIcon(':/image/bb3.ico'))
        # 是否在任务栏显示
        self.tray.setVisible(True)
        # 设置鼠标悬停显示信息
        self.tray.setToolTip('宝宝云平台')

        # 设置任务栏程序的菜单
        self.menu = QMenu()

        # 设置菜单列表
        self.quitAction = QAction()
        self.quitAction.setText('退出')
        self.quitAction.setIcon(QIcon(':/image/tc.ico'))

        # 添加进tray
        self.menu.addAction(self.quitAction)
        self.tray.setContextMenu(self.menu)

        # 菜单的点击事件
        self.quitAction.triggered.connect(self.quit)



    # 退出程序
    def quit(self):
        # "保险起见，为了完整的退出"
        self.tray.setVisible(False)
        # self.tray.parent().exit()
        #  qApp.quit()
        sys.exit()

    # 主页面按钮点击事件
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

        # 添加材料点击事件
        self.main.pushButton_26.clicked.connect(self.showMaterials)
        self.main.pushButton_28.clicked.connect(self.showNewMaterials)

        self.main.pushButton_24.clicked.connect(self.showAddEquipment)

    # 显示新增材料的窗口
    def showNewMaterials(self):
        self.newMaterialMain = QMainWindow()
        self.newMaterial = newMaterialView.Ui_MainWindow()
        self.newMaterial.setupUi(self.newMaterialMain)
        # 设置登录框的图标
        self.newMaterialMain.setWindowIcon(QIcon(':/image/大数据1.png'))
        # 禁止最大化
        self.newMaterialMain.setFixedSize(self.newMaterialMain.width(), self.newMaterialMain.height())
        self.newMaterialMain.show()
        self.newMaterial.pushButton.clicked.connect(self.newMaterials)

    def newMaterials(self):
        materialModel = newMaterialModel(self.newMaterial, self.cache)
        res = materialModel.run(self.newMaterial.lineEdit.text(), self.newMaterial.lineEdit_2.text(),
                                self.newMaterial.lineEdit_3.text())
        data = json.loads(res.text)
        if res.status_code == 200:
            QMessageBox.about(self,  # 使用infomation信息框
                              "信息",
                              "添加成功")
            print(data['msg'])
        else:
            QMessageBox.warning(self,  # 使用infomation信息框
                                "信息",
                                "添加失败",
                                QMessageBox.Yes)
            print(data['msg'])

    # 显示添加材料窗口
    def showAddEquipment(self):
        self.equipmentlMain = QMainWindow()
        self.equipment = add_equipment.Ui_MainWindow()
        self.equipment.setupUi(self.equipmentlMain)
        # 设置登录框的图标
        self.equipmentlMain.setWindowIcon(QIcon(':/image/大数据1.png'))
        # 禁止最大化
        self.equipmentlMain.setFixedSize(self.equipmentlMain.width(), self.equipmentlMain.height())
        self.equipmentlMain.show()

    # 添加材料
    def showMaterials(self):

        self.materialMain = QMainWindow()
        self.material = add_material.Ui_MainWindow()
        self.material.setupUi(self.materialMain)
        # 设置登录框的图标
        self.materialMain.setWindowIcon(QIcon(':/image/大数据1.png'))
        # 禁止最大化
        self.materialMain.setFixedSize(self.materialMain.width(), self.materialMain.height())
        # print(self.material.comboBox.currentText())
        materialModel = MaterialModel(self.material, self.cache)
        materialModel.run()

        self.material.pushButton.clicked.connect(self.addMaterials)

        self.materialMain.show()

    def addMaterials(self):
        from app.server.material import Material as MaterialServer
        text = self.material.comboBox.currentText()
        num = self.material.lineEdit.text()
        param = {'name': text, "num": num}
        material = MaterialServer(self.cache)
        data = material.addMaterial(param)
        if data.status_code == 200:
            QMessageBox.about(self,  # 使用infomation信息框
                              "信息",
                              "添加成功")
            data = json.loads(data.text)
            print(data)
        else:
            QMessageBox.warning(self,  # 使用infomation信息框
                                "信息",
                                "添加失败",
                                QMessageBox.Yes)

    # 查询
    def searh(self):
        text = self.main.lineEdit.text()
        print(text)

    # 产妇管理
    def showUser(self):
        self.main.tabWidget.setCurrentIndex(0)
        UserModel = userModel(self.main, self.cache)
        UserModel.run()

    # 医院管理
    def showHospital(self):
        self.main.tabWidget.setCurrentIndex(1)

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
        materail = MaterialModel(self.main, self.cache)
        materail.setMaterial()

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
