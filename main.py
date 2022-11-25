import geocoder
import requests


def get_gps_coordinates():
    g = geocoder.ip('me')
    return g.latlng


def get_weather(coordinates):
    if coordinates is None:
        raise Exception("Can't get coordinates")
    lt, ln = coordinates
    url_api = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current_weather=true"
    weather_dict = requests.get(url_api.format(lt, ln)).json()
    return weather_dict


def weather_formatter():
    coords = get_gps_coordinates()
    weather_dict = get_weather(coords)
    current_temperature = weather_dict['current_weather']['temperature']
    return f'Current temperature is {current_temperature} degrees Celsium'


if __name__ == "__main__":
    result = weather_formatter()
    print(result)
