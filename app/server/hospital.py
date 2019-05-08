"""
 Hello 

"""
import requests

from app.config.setting import BASE_URL


class hospital():
    def __init__(self,cache):
        self.cache = cache
        self.header = {"token": self.cache.get("token")}

    def getHospitalAll(self):
        url = BASE_URL + "/hospital/get"
        res = requests.get(url=url, headers=self.header)
        return res
