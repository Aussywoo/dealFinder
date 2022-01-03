import urllib3
import json

def get(itemName:str):
    http = urllib3.PoolManager()

    # Create appropriate URL
    url:str = 'https://offerup.com/api/search/v6/feed?limit=100&is_shippable_only=true&q=' + itemName

    # Submitting the get request using urllib3, because nothing else works for OfferUp
    resp = http.request('GET', url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'})
    data = json.loads(resp.data)

    # For testing only, print out Item Name and Location of all results
    feedItems = data['data']['feed_items']
    for item in feedItems:
        print(item['item']['title'] + ', ' + item['item']['location_name'])

def getData(itemName:str) -> list:
    get(itemName)
