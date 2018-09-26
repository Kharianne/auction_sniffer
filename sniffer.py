from email_sending import Email
from auction import get_auction_data, Item
import argparse


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--item_id', action='store', type=int, required=True)
    parser.add_argument('--user_min', action='store', type=int, required=True)
    parser.add_argument('--realm', action='store', type=str, required=True)
    parser.add_argument('--recipient', action='store', type=str, required=True)
    return vars(parser.parse_args())


if __name__ == '__main__':
    payload = {
        "locale": "en_GB",
        "apikey": "43t9t32j3d56sw9pdtfr55awmwkfzu88"
        }
    arguments = argument_parser()
    auction_data = get_auction_data(arguments['realm'], payload)
    if Item(arguments['item_id'], auction_data).is_price_higher_than(arguments['user_min']):
        Email('smtp.gmail.com: 587').send_email(arguments['recipient'], 'test', 'test')
