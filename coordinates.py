import geocoder
from typing import NamedTuple


class Coords(NamedTuple):
    latitude: float
    longitude: float
    city: str


def get_coordinates() -> Coords:
    """Returns current coordinates using ip"""
    g = geocoder.ip('me')
    try:
        lat, lng = g.latlng
        city = g.city
    except TypeError as e:
        print("Cannot get coordinates from ip. Check your Internet connection")
        raise e
    return Coords(lat, lng, city)


get_coordinates()
