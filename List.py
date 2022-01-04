""" A central class with functions to add search results to a list"""
from listing import Listing

mainList: list[Listing] = []


def addItem(itemName: str, location: str, price: float, date: str, imageURL: str, postURL: str, origin: str):
    """
    Adds a search result to the total list
    :param itemName: The name of the item
    :param location: The location of the listing
    :param price: The price of the item
    :param date: The date the listing was posted
    :param imageURL: The url of the image of the item
    :param postURL: The url of the original listing
    :param origin: The origin platform of the post
    :return: None
    """
    mainList.append(Listing(origin, itemName, location, date, price, imageURL, postURL))


def getList() -> list:
    """
    Returns the list of all search results
    :return: The main list containing all the items
    """
    return mainList


def getSortedList() -> list:
    """
    Returns a sorted list of all search results
    :return: The main list, but sorted!
    """
    return []


def getStore(origin: str) -> list:
    """
    Returns all search results from a particular store
    :param origin: The origin platform to search
    :return: A list of all listing from the specified origin platform
    """
    return [i for i in mainList if i.platform == origin] # List comprehension
