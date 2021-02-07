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
        """
        Comment: gets all data
        Input: Name of Instance
        Output: All Data available
        Special: Json data might be quite a bit
        """
        url = self.base
        r = requests.get(url)
        return json.loads(r.content)

    def get_current(self):
        """
        Comment: gets the last available data
        Input: Name of Instance
        Output: All available current data (only for the current day)
        Special: Nothing Special
        """
        url = self.base + "date"
        r = requests.get(url)
        return json.loads(r.content)

    def get_data_date(self, date):
        """
        Comment: gets all data for a certain day
        Input: Name of instance, date
        Output: Data as Json
        Special: Date format: Year-Month-Day
        """
        temp_url = self.base + "date/{date}"
        url = temp_url.format(date=date)
        r = requests.get(url)
        return json.loads(r.content)

    def get_data_county(self, county_id=None):
        """
        Comment: get all data for a certain county, without county all data
        Input: Name of Instance, optional: county_id
        Output: Server Response as Json
        Special: If no county_id is given, all data will be returned
        """
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
