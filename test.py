import requests

user = "get weather in bangalore"

if "weather" in user:
    response = requests.get("https://api.weather.com/xyz")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:")
        print(response.text)