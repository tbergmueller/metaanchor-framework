import json

class TemporaryDatabase:
    def __init__(self):
        with open('conf/tmpdb.json') as f:
            self._data = json.load(f)

    def getImageName(self, slid_b36):
        if slid_b36 in self._data["img_per_base36_slid"]:
            return self._data["img_per_base36_slid"][slid_b36]
        return None

    def getAttributes(self, slid_b36):
        if slid_b36 in self._data["att_per_base36_slid"]:
            return self._data["att_per_base36_slid"][slid_b36]
        return []
