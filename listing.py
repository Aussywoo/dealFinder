"""This module contains listing related classes"""

from datetime import datetime


class Listing:
    """
    A listing of an item from a platform
    """
    def __init__(self, platform: str, name: str, location: str, time: str, price: float, image_url: str, post_url: str):
        """
        Instantiates a Listing object
        :param platform: The platform an item was listed on
        :param name: The name of the item
        :param location: The location of the listing
        :param time: The time the listing was posted
        :param price: The price of the item
        :param image_url: A link to an image of the item
        :param post_url: A link to the original post
        """
        self.platform: str = platform
        self.name: str = name
        self.location: str = location
        self.price: float = price
        self.img: str = image_url
        self.postURL: str = post_url
        self.time = self.format_date(time)

    def format_date(self, date: str) -> datetime:
        """
        Formats the date provided from the website.
        :param date: The date string returned from the API
        :return: A python datetime object corresponding to the input
        """
        return datetime.fromisoformat(date)

    def __repr__(self):
        return f"Name: {self.name} from {self.platform}\n" \
               f"\tLocation: {self.location}\n" \
               f"\tPost Time: {self.time.strftime('%m/%d/%Y, %H:%M:%S')}\n" \
               f"\tPrice: ${self.price}\n" \
               f"\tImage Link: {self.img}\n" \
               f"\tPost Link: {self.postURL}\n"


class OfferUpListing(Listing):
    """
    A listing of an item from OfferUp
    """
    def format_date(self, date: str) -> datetime: return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

