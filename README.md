# WoW auction sniffer 
Enhance your auction experience with this simple python script. Set items to watch in config file and when auction price is higher
than your expected rate, you will recieve emai. This script is meant to be used on cron basis, but you can run it and you don't have to
run WoW or you just don't need to seek out auction house. 

For now, the script is made from auctioneer point of view - so it watches for given price level and when is high as you expectations you
will recieve email and you can go sell your precious items. Don't sell your items under price level again!

## Configuration file
### API section 
* ```client_id``` and ``` client_secret ```: these should be obtained from https://develop.battle.net/ 
* ```realm```: choose your realm name, eg.: "Chamber of Aspects" 
* ```localization```: US or EU 

### Email credentials section
I strongly recommend that you should create completelly new email for this purpose. To be able use this script, you have to
allow less secure apps (that's the reason why new email) via https://myaccount.google.com/lesssecureapps if you are using gmail.com. 
* ```from```: whole email adress of your new account
* ```password```: password 
* ```server```: email server, gmail: smtp.gmail.com:587
* ```to```: your email to receive notification mail

### Items section
You can place as many items as you want. 
* ```name```: it's voluntary, but basically item name from WoW
* ```id```: id of item, best way to get id is on wowhead (every item id is in url of item)
* ```price```: price is represented as list: [0,0,0] - [gold, silver, copper] so if you want to look for item price higher than 
25 gold 12 silver and 10 copper, your price list should look like this [25, 12, 10]. Do not ommit 0s! For 5 silvers use [0,5,0] etc.

## TO DO
* [ ] Add argparse for different config files - user will be able to run script with different configs
