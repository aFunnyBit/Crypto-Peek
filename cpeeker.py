#! /usr/bin/python3
import sys
import requests
import json

request = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0')
coin_dict = request.json()
coin_id = str(sys.argv[1])
results = 0

for x in coin_dict:
    if (x["id"] == coin_id or x['symbol'] == coin_id.upper()):
        results = json.dumps(x, indent = 4, sort_keys=True)
        break

print(results)


