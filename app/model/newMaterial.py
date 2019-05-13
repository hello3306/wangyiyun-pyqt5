"""
 Hello 

"""
import json

from app.server.material import Material as MaterialServer


class newMaterial():
    def __init__(self, material, cache):
        self.cache = cache
        self.material = material

    def run(self, name, Specifications, Company):
        param = {'name': name,
                 'Specifications': Specifications,
                 'Company': Company}
        Material = MaterialServer(self.cache)
        res = Material.newMaterial(param)
        data = json.loads(res.text)
        if res.status_code == 200:
            print(data['msg'])
        else:
            print(data['msg'])
