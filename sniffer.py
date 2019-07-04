from email_sending import Email
from new_api_auction import Data, Item, path
import json
from jinja2 import Template


def load_config():
    with open("config.json") as f:
        config = json.load(f)
        return config


if __name__ == '__main__':
    config = load_config()
    Data(config["api_credentials"]["localization"],
         config["api_credentials"]["client_id"],
         config["api_credentials"]["client_secret"],
         config["api_credentials"]["realm"],
         path).save_data()

    higher_price_items = list()
    for item in config["items"]:
        item_ob = Item(item["id"], path)
        if item_ob.is_price_higher_than(item["price"]):
            higher_price_items.append(item)
        elif item_ob.min_auction_price == 0:
            higher_price_items.append(item)

    if higher_price_items:
        with open("mail_template.txt") as f:
            template = Template(f.read())
        message = template.render(items=higher_price_items)

        Email(config["email_credentials"]["server"],
              config["email_credentials"]["password"],
              config["email_credentials"]["from"])\
            .send_email("katerinamrkackova@gmail.com",
                        'Results of auction sniffing', message)






