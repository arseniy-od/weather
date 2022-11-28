# Weather
This is Python program to get current weather in your location. It uses your ip to get coordinates and uses 
open_meteo.com api to get weather data.
## Installation
To install use git clone and install geocoder library
```bash
git clone https://github.com/arseniy-od/weather.git 
pip install geocoder
```

## Usage
To use this script run weather.py from project root
```bash
python weather.py
```
If you use UNIX shell you can make "weather" executable and add it to path
```bash
# example of program output
Temperature is 4 degrees Celsium
Weather type is Overcast
Sunrise is at 06:58
Sunset is at 15:52
City: Orikhiv
```