import urllib.request
import json
from json.decoder import JSONDecodeError
from urllib.error import URLError
from typing import NamedTuple
from datetime import datetime

import config
from coordinates import Coords, get_city
from exceptions import ApiServiceError


weather_type_codes = {
    0: 'Clear sky',
    1: 'Mainly clear',
    2: 'Partly cloudy',
    3: 'Overcast',
    45: 'Fog',
    48: 'Depositing rime fog',
    51: 'Light drizzle',
    53: 'Moderate drizzle',
    55: 'Dense intensity drizzle',
    56: 'Light Freezing Drizzle',
    57: 'Dense intensity Freezing Drizzle',
    61: 'Slight rain',
    63: 'Moderate rain',
    65: 'Heavy intensity rain',
    66: 'Light Freezing Rain',
    67: 'Heavy intensity Freezing Rain',
    71: 'Slight snow fall',
    73: 'Moderate snow fall',
    75: 'Heavy intensity snow fall',
    77: 'Snow grains',
    80: 'Slight rain showers',
    81: 'Moderate rain showers',
    82: 'Violent rain showers',
    85: 'Slight snow showers',
    86: 'Heavy snow showers',
    95: 'Thunderstorm: Slight or moderate',
    96: 'Thunderstorm with slight hail',
    99: 'Thunderstorm with heavy hail'
}

Celsium = int


class Weather(NamedTuple):
    temperature: Celsium
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coords) -> Weather:
    """Calls open-meteo.com api to get weather data using coordinates"""
    weather_dict = _parse_openmeteo_response(_get_openmeteo_response(coordinates))
    city = get_city()
    current_temperature = round(weather_dict['current_weather']['temperature'])
    weather_code = weather_dict['current_weather']['weathercode']
    weather_type = weather_type_codes[weather_code]

    weekday = datetime.today().weekday()
    sunrise_ts = weather_dict['daily']['sunrise'][weekday]
    sunset_ts = weather_dict['daily']['sunset'][weekday]
    sunrise_dt = datetime.fromtimestamp(sunrise_ts)
    sunset_dt = datetime.fromtimestamp(sunset_ts)

    weather = Weather(current_temperature, weather_type, sunrise_dt, sunset_dt, city)

    return weather


def _get_openmeteo_response(coordinates: Coords) -> bytes:
    latitude, longitude = coordinates.latitude, coordinates.longitude
    try:
        response = urllib.request.urlopen(config.URL_API.format(latitude=latitude, longitude=longitude)).read()
    except URLError:
        raise ApiServiceError
    return response


def _parse_openmeteo_response(weather_dict_raw: bytes) -> dict:
    try:
        weather_dict = json.loads(weather_dict_raw)
    except JSONDecodeError:
        raise ApiServiceError
    return weather_dict