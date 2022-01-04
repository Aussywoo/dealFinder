from datetime import datetime


class Listing():
    def __init__(self, platform: str, name: str, location: str, time: str, price: str, img: str):
        self.platform: str = platform
        self.name: str = name
        self.location: str = location
        self.price: float = float(price)
        self.img: str = img
        self.time = self.format_date(time)

    def format_date(self, date: str) -> datetime: return datetime.fromisoformat(date)

    def get_url(self) -> str:
        return 'https://google.com/'

    def __repr__(self):
        return f"Name: {self.name} from {self.platform}\n" \
               f"\tLocation: {self.location}\n" \
               f"\tPost Time: {self.time.strftime('%m/%d/%Y, %H:%M:%S')}\n" \
               f"\tPrice: {self.price}\n" \
               f"\tImage Link: {self.img}\n"

class OfferupListing(Listing):
    def format_date(self, date: str) -> datetime: return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

