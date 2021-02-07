import requests
import json

class Wrapper():
    def __init__(self):
        """
        Comment: standard init
        Input: name of instanze
        Output: Nothing
        Special: Nothing
        """
        self.base = "https://europe-west3-brdata-corona.cloudfunctions.net/lglApi/"

    def get_data(self):
        # TODO: add docu
        r = requests.get(self.base)
        return json.loads(r.content)
