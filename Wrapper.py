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
        url = self.base
        r = requests.get(url)
        return json.loads(r.content)

    def get_current(self):
        # TODO: add docu
        url = self.base + "date"
        r = requests.get(url)
        return json.loads(r.content)

    def get_data_date(self, date):
        # TODO: add dpcu
        temp_url = self.base + "date/{date}"
        url = temp_url.format(date=date)
        r = requests.get(url)
        return json.loads(r.content)

    def get_data_county(self, county_id=None):
        # TODO: add docu
        if county_id:
            temp_url = self.base + "county/{county_id}"
            url = temp_url.format(county_id=county_id)
        else:
            url = self.base + "county"
        r = requests.get(url)
        return json.loads(r.content)




def main():
    test = Wrapper()
    x = test.get_data_county("altoetting")
    json.dump(x, open("out.json", "w"))
    # total = 0
    # total_new = 0
    # for point in x:
    #     add = point["cases"] - point["previous-cases"]
    #     total_new+=add
    #     total+= point["cases"]
    # print(total_new)
    # print(total)


if __name__ == '__main__':
    main()
