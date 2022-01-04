from datetime import datetime


class Listing():
    def __init__(self, platform: str, name: str, location: str, time: str, price: str, img: str):
        self.platform: str = platform
        self.name: str = name
        self.location: str = location
        self.price: float = float(price)
        self.img: str = img
        try: self.time = datetime.fromisoformat(time)
        except: self.time = datetime.min

    def __repr__(self):
        return f"Name: {self.name} from {self.platform}\n" \
               f"\tLocation: {self.location}\n" \
               f"\tPost Time: {self.time.strftime('%m/%d/%Y, %H:%M:%S')}\n" \
               f"\tPrice: {self.price}\n" \
               f"\tImage Link: {self.img}\n"

class OfferupListing(Listing):
    def __init__(self, platform: str, name: str, location: str, time: str, price: str, img: str):
        super().__init__(platform, name, location, time, price, img)
        self.time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')