#!usr/bin/env python
from weather_formatter import weather_formatter
from coordinates import get_coordinates
from get_weather import get_weather


if __name__ == "__main__":
    coords = get_coordinates()
    weather = get_weather(coords)
    result = weather_formatter(weather)
    print(result)
