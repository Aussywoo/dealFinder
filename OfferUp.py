"""This module contacts OfferUp for information"""

import json
import rest
from listing import Listing, OfferUpListing

item_list: list[Listing] = []


# Returns a list with all search results from OfferUp
def get(item_name: str, items: int = 100) -> list[Listing]:
    """
    Returns a list with all search results from OfferUp
    :param items: The number of items to search for
    :param item_name: The search term to query
    :return: A list of Listings from the offerup
    """
    # Create appropriate URL
    url: str = 'https://offerup.com/api/search/v6/feed'

    # Submitting the get request using urllib3, because nothing else works for OfferUp
    data = json.loads(rest.make_request_urllib3('GET', url, {'User-Agent': rest.user_agent_str},
                                                {
                                                    'limit': str(items),
                                                    'is_shippable_only': 'true',
                                                    'q': item_name
                                                }).data)

    # Adds all search results to itemList
    feedItems = data['data']['feed_items']
    for item in feedItems:
        item_list.append(OfferUpListing('OfferUp', item['item']['title'], item['item']['location_name'],
                                        item['item']['post_date'],
                                        float(item['item']['price']),
                                        item['item']['photos'][0]['images']['detail']['url'],
                                        'https://offerup.com/item/detail/' + item['item']['listing_id']))
    return item_list
