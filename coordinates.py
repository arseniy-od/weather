import geocoder
import config
from typing import NamedTuple
from exceptions import CantGetCoordinates


class Coords(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coords:
    """Returns current coordinates using ip"""
    g = _get_geocoder_query()
    lat, lng = g.latlng
    coords = Coords(lat, lng)
    if config.ROUND_COORDINATES:
        coords = _round_coords(coords)
    return coords


def get_city() -> str:
    g = _get_geocoder_query()
    return g.city


def _get_geocoder_query():
    g = geocoder.ip('me')
    if g.error:
        raise CantGetCoordinates
    return g


def _round_coords(coords: Coords) -> Coords:
    """Rounds latitude and longitude to 1 decimal point"""
    coords = Coords(round(coords.latitude, 1), round(coords.longitude, 1))
    return coords


if __name__ == "__main__":
    print(get_coordinates())
