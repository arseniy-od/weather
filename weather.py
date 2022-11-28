from weather_formatter import weather_formatter
from coordinates import get_coordinates
from get_weather import get_weather
from exceptions import CantGetCoordinates, ApiServiceError


def main():
    try:
        coords = get_coordinates()
    except CantGetCoordinates:
        print("Can't get coordinates")
        raise SystemExit(1)
    try:
        weather = get_weather(coords)
    except ApiServiceError:
        print("Can't get data from api service")
        raise SystemExit(1)
    print(weather_formatter(weather))


if __name__ == "__main__":
    main()
