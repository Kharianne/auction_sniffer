import requests
import os
import json

path = "{}/auction_data".format(os.getcwd())


class Data:
    def __init__(self, localization, client_id, client_secret, realm, path):
        self.localization = localization
        self.client_id = client_id
        self.client_secret = client_secret
        self.realm = realm
        self.path = path

        self.auth_token = None
        self.data_info = None

    def get_auth_token(self):
        payload = {"grant_type": "client_credentials",
                   "client_id": self.client_id,
                   "client_secret": self.client_secret}
        url = "https://{}.battle.net/oauth/token".format(self.localization)
        request = requests.post(url, params=payload)
        return request.json()["access_token"]

    def get_data_info(self):
        url = "https://{}.api.blizzard.com/wow/auction/data/{}".format(self.localization, self.realm)
        payload = {"locale": "enUS",
                   "access_token": self.auth_token}
        request = requests.get(url, params=payload)
        # TODO: add more files validation
        return request.json()["files"][0]

    def is_the_latest(self):
        files = []
        for file in os.listdir(self.path):
            files.append(int(file.split('.')[0]))
        return False if max(files) >= self.data_info["lastModified"] else True

    def save_data(self):
        self.auth_token = self.get_auth_token()
        self.data_info = self.get_data_info()
        if self.is_the_latest():
            try:
                os.mkdir(self.path)
            except FileExistsError:
                "Folder already created"
            data_json = requests.get(self.data_info["url"]).json()["auctions"]
            with open("{}/{}.json".format(self.path, self.data_info["lastModified"]), "w+") as f:
                json.dump(data_json, f)
        else:
            return "Already file with the newest data"


class Item:
    def __init__(self, item_id, path):
        self.item_id = item_id
        self.item_array = list()
        self.path = path
        self.data = None
        self.min_auction_price = self.get_min_auction_price()

    def prepare_data(self):
        files = os.listdir(self.path)
        if not files:
            return "There are no files"
        else:
            files = []
            for file in os.listdir(self.path):
                files.append(int(file.split('.')[0]))
            with open("{}/{}.json".format(self.path, max(files))) as data_file:
                self.data = json.load(data_file)

    def get_min_auction_price(self):
        self.prepare_data()
        for item in self.data:
            if item["item"] == self.item_id:
                self.item_array.append(item)
        if self.item_array:
            return min(self.item_array, key=lambda x: x["buyout"])["buyout"]
        else:
            return 0

    def is_price_higher_than(self, user_min):
        if len(user_min) == 3:
            try:
                user_min = user_min[0] * 10000 + user_min[1]*100 + user_min[2]
            except TypeError:
                return "Price is not an int."

            return True if self.min_auction_price > user_min else False
        else:
            return "Missing price arguments"
