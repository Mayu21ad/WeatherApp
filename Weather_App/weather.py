
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather():
    print('\n*** The Weather ***\n')

    city = input("\nCity name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={os.getenv("API_KEY")}'

    weather_data = requests.get(request_url).json()

    print("City:", city)

    if 'main' in weather_data:
    
        temperature = weather_data['main'].get('temp')
        
        if temperature is not None:
            print(f'\nThe temp is {temperature:.1f}°')
            print(f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')
        else:
            print("Temperature data not found in the 'main' section of the API response.")
    else:
        print("No 'main' section found in the API response.")

get_current_weather()
