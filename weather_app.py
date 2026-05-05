# Weather App
# Author: Muhammad Ameen J
# Description: Real-time weather data using OpenWeatherMap API
 
import requests

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
 
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
 
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
 
        if data["cod"] != 200:
            print(f"\n  ❌ Error: {data['message'].capitalize()}")
            return
 
        # Extract data
        city_name    = data["name"]
        country      = data["sys"]["country"]
        temp         = data["main"]["temp"]
        feels_like   = data["main"]["feels_like"]
        temp_min     = data["main"]["temp_min"]
        temp_max     = data["main"]["temp_max"]
        humidity     = data["main"]["humidity"]
        pressure     = data["main"]["pressure"]
        wind_speed   = data["wind"]["speed"]
        description  = data["weather"][0]["description"].title()
        visibility   = data.get("visibility", 0) // 1000  # Convert to km
 
        # Display
        print("\n" + "=" * 50)
        print(f"  📍 {city_name}, {country}")
        print("=" * 50)
        print(f"  🌤️  Condition     : {description}")
        print(f"  🌡️  Temperature   : {temp}°C  (Feels like {feels_like}°C)")
        print(f"  🔼  Max / Min     : {temp_max}°C / {temp_min}°C")
        print(f"  💧  Humidity      : {humidity}%")
        print(f"  🌬️  Wind Speed    : {wind_speed} m/s")
        print(f"  📊  Pressure      : {pressure} hPa")
        print(f"  👁️  Visibility    : {visibility} km")
        print("=" * 50)
 
        # Weather tip
        if temp < 15:
            print("  🧥 Tip: It's cold outside, carry a jacket!")
        elif temp > 35:
            print("  ☀️  Tip: Very hot! Stay hydrated.")
        elif "Rain" in description or "rain" in description:
            print("  ☂️  Tip: Carry an umbrella!")
        else:
            print("  😊 Tip: Weather looks good, enjoy your day!")
        print("=" * 50)
 
    except requests.exceptions.ConnectionError:
        print("\n  ❌ No internet connection. Please check your network.")
    except Exception as e:
        print(f"\n  ❌ Something went wrong: {e}")
 
def main():
    print("=" * 50)
    print("        🌦️  WEATHER APP")
    print("   Powered by OpenWeatherMap API")
    print("=" * 50)
 
    while True:
        city = input("\n  Enter city name (or 'quit' to exit): ").strip()
 
        if city.lower() in ["quit", "exit", "q"]:
            print("\n  Goodbye! Stay weather-aware! 👋")
            break
 
        if not city:
            print("  ⚠️  Please enter a valid city name.")
            continue
 
        get_weather(city)
 
if __name__ == "__main__":
    main()
 