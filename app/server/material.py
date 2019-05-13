"""
 Hello 

"""
import requests

from app.config.setting import BASE_URL


class Material():

    def __init__(self, cache):
        self.cache = cache
        self.header = {"token": self.cache.get("token")}

    def getAllMaterial(self):
        url = BASE_URL + "/Equipment/getAllMaterial"
        res = requests.get(url=url, headers=self.header)
        return res

    def newMaterial(self, param):
        url = BASE_URL + "/Equipment/newMaterial"
        res = requests.post(url=url, data=param, headers=self.header)
        return res
