import urllib3
import List
import json

itemList:list[list[str]] = []

# Returns a list with all search results from OfferUp
def get(itemName:str) -> list:
    http = urllib3.PoolManager()

    # Create appropriate URL
    url:str = 'https://offerup.com/api/search/v6/feed?limit=100&is_shippable_only=true&q=' + itemName

    # Submitting the get request using urllib3, because nothing else works for OfferUp
    resp = http.request('GET', url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'})
    data = json.loads(resp.data)

    # Adds all search results to itemList
    feedItems = data['data']['feed_items']
    for item in feedItems:
        itemList.append([item['item']['title'], item['item']['location_name'],
                         item['item']['post_date'],
                         item['item']['price'],
                         item['item']['photos'][0]['images']['detail']['url'],
                         'OfferUp'])
    return itemList