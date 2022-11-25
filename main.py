import geocoder
import requests
from typing import NamedTuple
from datetime import datetime


class Coords(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coords:
    """Returns current coordinates using ip"""
    g = geocoder.ip('me')
    try:
        lat, lng = g.latlng
    except TypeError as e:
        print("Cannot get coordinates from ip. Check your Internet connection")
        raise e
    return Coords(lat, lng)


def get_weather(coordinates: Coords):
    latitude, longitude = coordinates.latitude, coordinates.longitude
    url_api = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current_weather=true" \
              "&timeformat=unixtime&timezone=Africa%2FCairo"
    weather_dict = requests.get(url_api.format(latitude, longitude)).json()
    return weather_dict


def weather_formatter():
    coords = get_coordinates()
    weather_dict = get_weather(coords)
    print(weather_dict)
    current_temperature = round(weather_dict['current_weather']['temperature'])
    dt = datetime.fromtimestamp(weather_dict['current_weather']['time'])
    dt_str = dt.strftime("%d %b %Y - %H:%M")
    return f'Temperature at {dt_str} is {current_temperature} degrees Celsium'


if __name__ == "__main__":
    result = weather_formatter()
    print(result)
