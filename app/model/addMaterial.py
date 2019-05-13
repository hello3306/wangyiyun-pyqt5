"""
 Hello 

"""
import json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from app.server.material import Material as  MaterialServer


class addMaterial(QtWidgets.QWidget):
    def __init__(self, material, cache):
        self.material = material
        self.cache = cache


    def run(self):
        self.getAllMaterail()
        # self.material.pushButton.clicked.connect(self.add)

    def add(self):
        text = self.material.comboBox.currentText()
        num = int(self.material.lineEdit.text())
        if num == 0:
            QMessageBox.warning(self,  # 使用infomation信息框
                                "警告",
                                "数量不能为空",
                                QMessageBox.Yes)
        print("材料名：" + text + "数量：" + num)

    def getAllMaterail(self):
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
