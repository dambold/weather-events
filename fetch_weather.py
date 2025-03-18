import requests
import json

# Replace with your actual API key
API_KEY = "your_api_key"
CITY = "Tulsa"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
weather_data = response.json()

# Save data to a file
with open("weather_data.json", "w") as file:
    json.dump(weather_data, file, indent=4)

print("Weather data saved successfully!")

