import datetime as dt
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "YOUR_CITY"


def K_to_CF(temp):
    celcius = temp - 273.15
    fahrenheit = celcius * 9/5 + 32
    return celcius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_K = response["main"]["temp"]
temp_C, temp_F = K_to_CF(temp_K)

temp_feels_K = response["main"]["feels_like"]
temp_feels_C, temp_feels_F = K_to_CF(temp_feels_K)

wind_speed_ms = response["wind"]["speed"]

weather = response["weather"][0]["description"]
sun_rise = dt.datetime.fromtimestamp(response["sys"]["sunrise"])
sun_set = dt.datetime.fromtimestamp(response["sys"]["sunset"])

humidity = response["main"]["humidity"]

print(f"Current temperature in {CITY} is {temp_C:.2f} degrees Celsius.")
print(f"Current temperature in {CITY} is {temp_F:.2f} degrees Fahrenheit.")
print(f"Current feels like temperature in {CITY} is {temp_feels_C:.2f} degrees Celsius.")
print(f"Current feels like temperature in {CITY} is {temp_feels_F:.2f} degrees Fahrenheit.")
print("Wind speed in {} is {} m/s.".format(CITY, wind_speed_ms))
print("The weather in {} is {}.".format(CITY, weather))
print("The sun will rise at {} and set at {}.".format(sun_rise, sun_set))
print("The humidity in {} is {}%.".format(CITY, humidity))






