import geocoder
import requests
from collections import namedtuple

Coords = namedtuple('Coords', 'latitude longitude')


def get_gps_coordinates() -> Coords:
    """Returns current coordinates using ip"""
    g = geocoder.ip('me')
    try:
        lat, lng = g.latlng
    except TypeError as e:
        print("Cannot get coordinates from ip. Check your Internet connection")
        raise e
    return Coords(lat, lng)


def get_weather(coordinates):
    latitude, longitude = coordinates.latitude, coordinates.longitude
    url_api = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current_weather=true"
    weather_dict = requests.get(url_api.format(latitude, longitude)).json()
    return weather_dict


def weather_formatter():
    coords = get_gps_coordinates()
    weather_dict = get_weather(coords)
    current_temperature = weather_dict['current_weather']['temperature']
    return f'Current temperature is {current_temperature} degrees Celsium'


if __name__ == "__main__":
    result = weather_formatter()
    print(result)
