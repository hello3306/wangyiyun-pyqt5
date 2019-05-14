"""
 Hello 

"""
import json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView

from app.server.material import Material as MaterialServer


class addMaterial(QtWidgets.QWidget):
    def __init__(self, material, cache):
        self.material = material
        self.cache = cache

    def run(self):
        self.getAllMaterail()

    # 添加材料的数量
    def add(self):
        text = self.material.comboBox.currentText()
        num = self.material.lineEdit.text()
        param = {'name': text, "num": num}
        # material = MaterialServer(self.cache)
        # data = material.addMaterial(param)
        print(param)

    # 获取所有的材料
    def getAllMaterail(self):
        material = MaterialServer(self.cache)
        data = material.getAllMaterial()
        if data.status_code == 200:
            x = 0
            data = json.loads(data.text)
            for i in data['data']:
                self.material.comboBox.setItemText(x, i['name'])
                x += 1

    def setMaterial(self):
        material = MaterialServer(self.cache)
        data = material.getAllMaterial()
        if data.status_code == 200:
            x = 0
            data = json.loads(data.text)
            self.material.tableWidget_2.setRowCount(len(data['data']))
            # self.material.tableWidget.setColumnWidth(4, 150)
            self.material.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
            for i in data['data']:
                self.material.tableWidget_2.setItem(x, 0, QtWidgets.QTableWidgetItem(i['name']))
                self.material.tableWidget_2.setItem(x, 1, QtWidgets.QTableWidgetItem(i['Specifications']))
                self.material.tableWidget_2.setItem(x, 2, QtWidgets.QTableWidgetItem(i['Company']))
                self.material.tableWidget_2.setItem(x, 3, QtWidgets.QTableWidgetItem(str(i['num'])))
                x += 1
