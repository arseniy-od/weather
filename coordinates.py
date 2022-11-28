import geocoder
import config
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
    coords = Coords(lat, lng, city)
    if config.ROUND_COORDINATES:
        coords = _round_coords(coords)
    return coords


def _round_coords(coords: Coords) -> Coords:
    """Rounds latitude and longitude to 1 decimal point"""
    coords = Coords(round(coords.latitude, 1), round(coords.longitude, 1), coords.city)
    return coords
