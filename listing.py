from datetime import datetime


class Listing():
    def __init__(self, platform: str, name: str, location: str, time: str, price: float, img: str, postURL: str):
        self.platform: str = platform
        self.name: str = name
        self.location: str = location
        self.price: float = price
        self.img: str = img
        self.postURL: str = postURL
        self.time = self.format_date(time)

    def format_date(self, date: str) -> datetime: return datetime.fromisoformat(date)

    def __repr__(self):
        return f"Name: {self.name} from {self.platform}\n" \
               f"\tLocation: {self.location}\n" \
               f"\tPost Time: {self.time.strftime('%m/%d/%Y, %H:%M:%S')}\n" \
               f"\tPrice: ${self.price}\n" \
               f"\tImage Link: {self.img}\n" \
               f"\tPost Link: {self.postURL}\n"

class OfferupListing(Listing):
    def format_date(self, date: str) -> datetime: return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

