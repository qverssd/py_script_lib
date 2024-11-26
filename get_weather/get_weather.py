import requests
import os

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "city",
        "appid": api_key,
        "units": "metric",
        "lang": "en"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Current weather in {city}:\nTemperature: {temp}°C\nCondition: {description.capitalize()}")
    else:
        print("Failed to retrive data:", data.get("message", "Unknown error"))

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)