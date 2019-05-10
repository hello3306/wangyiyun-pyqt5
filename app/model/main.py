"""
 Hello 

"""
import json

from PyQt5 import QtWidgets

from app.model.user import userModel


class mainModel(QtWidgets.QWidget):
    def __init__(self, main):
        self.main = main
        self.cache = ''

    def run(self):
        # 按钮点击事件
        self.main.pushButton.clicked.connect(self.showUser)
        self.main.pushButton_2.clicked.connect(self.showHospital)
        self.main.pushButton_3.clicked.connect(self.showEquipment)
        self.main.pushButton_4.clicked.connect(self.showCord)
        self.main.pushButton_5.clicked.connect(self.showMsg)
        self.main.pushButton_6.clicked.connect(self.showInformation)
        self.main.pushButton_7.clicked.connect(self.showOrder)
        self.main.pushButton_8.clicked.connect(self.showMaterial)
        self.main.pushButton_15.clicked.connect(self.searh)

    # 查询
    def searh(self):
        text = self.main.lineEdit.text()
        print(text)

    # 产妇管理
    def showUser(self):
        from app.server.user import User
        self.main.tabWidget.setCurrentIndex(0)
        user = User(self.cache)
        res = user.getUserInfo()
        if res.status_code == 200:
            data = json.loads(res.text)
            UserModel = userModel(self.main, data)
            UserModel.setData()
            # print(data['data'])

        else:
            print("请求失败")
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
