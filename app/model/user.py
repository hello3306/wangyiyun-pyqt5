"""
 Hello 

"""
import datetime
import json
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QAbstractItemView

from app.server.user import User




class userModel(QtWidgets.QWidget):
    def __init__(self, main, cache):
        self.main = main
        self.cache= cache

    def run(self):
        # self.thread = RunThread(self.cache)
        # self.thread.start()
        # self.thread.pButton.connect(self.setDatas)
        userServer = User(self.cache)
        res = userServer.getUserInfo()
        if res.status_code == 200:
            self.setData(res.text)

    def setDatas(self, res):
        print(res)

    def setData(self, res):
        x = 0
        if res:
            data = json.loads(res)
            self.main.tableWidget.setRowCount(len(data['data']))
            self.main.tableWidget.setColumnWidth(4, 150)
            self.main.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            for i in data['data']:
                self.main.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(i['user_name']))
                self.main.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(i['mobile']))
                self.main.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(i['hospital_id'])))
                self.main.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(self.time(i['predicted_time']))))
                self.main.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(i['create_time']))
                self.main.tableWidget.setItem(x, 5, QtWidgets.QTableWidgetItem(self.status(int(i["index"]))))
                self.main.tableWidget.setItem(x, 8, QtWidgets.QTableWidgetItem(str(i['status'])))
                self.main.label_17.setText('32')
                x += 1

    # 产妇状态
    def status(self, index):
        if index == 1:
            status = "待完善"
        elif index == 2:
            status = '已完善'
        elif index == 3:
            status = '待制作'
        elif index == 4:
            status = '制作中'
        elif index == 5:
            status = '待审核'
        else:
            status = '已发布'
        return status

    # 时间戳转换为时间格式
    def time(self, data):
        return (datetime.datetime.utcfromtimestamp(int(data))).strftime("%Y-%m-%d ")

#
# class RunThread(QThread):
#     pButton = pyqtSignal(str)
#
#     def __init__(self, cache):
#         self.cache = cache
#         super(RunThread, self).__init__()
#
#     def run(self):
#         if self.cache:
#             userServer = User(self.cache)
#             res = userServer.getUserInfo()
#             if res.status_code == 200:
#                 time.sleep(1)
#                 self.pButton.emit(str(res.text))
#
#     def callback(self, msg):
#         # 信号焕发，我是通过我封装类的回调来发起的
#         pass
