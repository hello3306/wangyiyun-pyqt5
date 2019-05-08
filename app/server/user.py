"""
 Hello 

"""
import requests

from app.config.setting import BASE_URL


class User():
    def __init__(self, cache):
        self.cache = cache
        self.header = {"token": self.cache.get("token")}

    def getUserInfo(self):
        url = BASE_URL + "/user"
        res = requests.get(url=url, headers=self.header)
        return res
