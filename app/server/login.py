"""
 Hello 

"""

import requests
from app.config.setting import *


class Login():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def run(self):
        param = {'name': self.user, 'password': self.password}
        url = BASE_URL + "/token/agent"
        res = requests.post(url=url, data=param)
        return res
