from urllib.parse import quote
import requests

# realm_name = quote("Chamber of Aspects")
# url = "https://eu.api.battle.net/wow/auction/data/" + realm_name
# payload = {
#   "locale": "en_GB",
#   "apikey": "43t9t32j3d56sw9pdtfr55awmwkfzu88"
# }


def get_auction_data(realm_name, payload):
    realm_name = quote(realm_name)
    url = "https://eu.api.battle.net/wow/auction/data/" + realm_name
    url_request = requests.get(url, params=payload)
    data_url = url_request.json()["files"][0]["url"]
    data_request = requests.get(data_url)
    return data_request.json()


class Item:
    def __init__(self, item_id, data):
        self.item_id = item_id
        self.data = data
        self.item_array = list()

        for item in data["auctions"]:
            if item["item"] == self.item_id:
                self.item_array.append(item)
        self.min_auction_price = min(self.item_array, key=lambda x: x["buyout"])["buyout"]

    def is_price_higher_than(self, user_min):
        return True if self.min_auction_price > user_min else False

