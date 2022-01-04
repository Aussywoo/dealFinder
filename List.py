""" A central class with functions to add search results to a list"""
from listing import Listing

mainList: list[Listing] = []


def add_item(item_name: str, location: str, price: float, date: str, image_url: str, post_url: str, origin: str):
    """
    Adds a search result to the total list
    :param item_name: The name of the item
    :param location: The location of the listing
    :param price: The price of the item
    :param date: The date the listing was posted
    :param image_url: The url of the image of the item
    :param post_url: The url of the original listing
    :param origin: The origin platform of the post
    :return: None
    """
    mainList.append(Listing(origin, item_name, location, date, price, image_url, post_url))


def get_list() -> list:
    """
    Returns the list of all search results
    :return: The main list containing all the items
    """
    return mainList


def get_sorted_list() -> list:
    """
    Returns a sorted list of all search results
    :return: The main list, but sorted!
    """
    return []


def get_store(origin: str) -> list:
    """
    Returns all search results from a particular store
    :param origin: The origin platform to search
    :return: A list of all listing from the specified origin platform
    """
    return [i for i in mainList if i.platform == origin]  # List comprehension
