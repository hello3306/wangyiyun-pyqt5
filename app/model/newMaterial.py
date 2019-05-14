"""
 Hello 

"""
import json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from app.server.material import Material as MaterialServer


class newMaterial(QtWidgets.QWidget):
    def __init__(self, material, cache):
        self.cache = cache
        self.material = material

    def run(self, name, Specifications, Company):
        param = {'name': name,
                 'Specifications': Specifications,
                 'Company': Company}
        Material = MaterialServer(self.cache)
        res = Material.newMaterial(param)

        return res
