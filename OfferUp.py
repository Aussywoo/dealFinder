import urllib3
import List
import json

from listing import Listing, OfferupListing
import rest

itemList: list[Listing] = []


# Returns a list with all search results from OfferUp
def get(itemName: str) -> list[Listing]:
    # Create appropriate URL
    url: str = 'https://offerup.com/api/search/v6/feed'

    # Submitting the get request using urllib3, because nothing else works for OfferUp
    data = json.loads(rest.make_request_urllib3('GET', url, {'User-Agent': rest.user_agent_str},
                                                {
                                                    'limit': '100',
                                                    'is_shippable_only': 'true',
                                                    'q': itemName
                                                }).data)

    # Adds all search results to itemList
    feedItems = data['data']['feed_items']
    for item in feedItems:
        itemList.append(OfferupListing('OfferUp', item['item']['title'], item['item']['location_name'],
                                item['item']['post_date'],
                                float(item['item']['price']),
                                item['item']['photos'][0]['images']['detail']['url'],
                                       'https://offerup.com/item/detail/' +  item['item']['listing_id']))
    return itemList
