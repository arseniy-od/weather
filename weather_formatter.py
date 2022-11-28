from get_weather import Weather, get_weather

WEATHER_TEMPLATE = """
Temperature is {0} degrees Celsium
Weather type is "{1}"
Sunrise is at {2}
Sunset is at {3}
City: {4}
"""


def dt_to_str(dt):
    return dt.strftime("%H:%M")


def weather_formatter(weather: Weather) -> str:
    """Formats weather data to string"""
    sunrise = dt_to_str(weather.sunrise)
    sunset = dt_to_str(weather.sunset)
    weather_str = WEATHER_TEMPLATE.format(weather.temperature, weather.weather_type, sunrise, sunset, weather.city)
    return weather_str




