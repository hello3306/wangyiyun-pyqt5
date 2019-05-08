"""
 Hello 

"""
import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView


class userModel(QtWidgets.QWidget):
    def __init__(self, main, data):
        self.main = main
        self.data = data

    def setData(self):
        self.main.tableWidget.setRowCount(len(self.data['data']))
        self.main.tableWidget.setColumnWidth(4, 150)
        self.main.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        x = 0

        for i in self.data['data']:
            self.main.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(i['user_name']))
            self.main.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(i['mobile']))
            self.main.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(i['hospital_id'])))
            self.main.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(self.time(i['predicted_time']))))
            self.main.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(i['create_time']))
            self.main.tableWidget.setItem(x, 5, QtWidgets.QTableWidgetItem(self.status(int(i["index"]))))
            self.main.tableWidget.setItem(x, 8, QtWidgets.QTableWidgetItem(str(i['status'])))
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

    # 时间戳转换为时间格式釦
    def time(self, data):
        return (datetime.datetime.utcfromtimestamp(int(data))).strftime("%Y-%m-%d ")
