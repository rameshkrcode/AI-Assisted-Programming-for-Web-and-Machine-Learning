
import requests
# AI-generated snippet for API integration:
def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    response = requests.get(base_url, params=params)
    return response.json()
print(get_weather("New York"))
