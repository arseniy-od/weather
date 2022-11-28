import geocoder
from typing import NamedTuple
from exceptions import CantGetCoordinates


class Coords(NamedTuple):
    latitude: float
    longitude: float
    city: str


def get_coordinates() -> Coords:
    """Returns current coordinates using ip"""
    g = geocoder.ip('me')
    if g.error:
        raise CantGetCoordinates("Cannot get coordinates from ip. Check your Internet connection")
    lat, lng = g.latlng
    city = g.city
    return Coords(lat, lng, city)
