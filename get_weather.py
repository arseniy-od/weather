import requests
from typing import NamedTuple
from datetime import datetime
from coordinates import Coords


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
    latitude, longitude = coordinates.latitude, coordinates.longitude
    url_api = 'https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&daily=sunrise,sunset' \
              '&current_weather=true&timeformat=unixtime&timezone=Africa%2FCairo'
    weather_dict = requests.get(url_api.format(latitude, longitude)).json()

    city = coordinates.city
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
