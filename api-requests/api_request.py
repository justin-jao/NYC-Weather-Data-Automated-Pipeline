import requests
api_key = "a1ccb6e53249a23fbd5f4d062bbf39b7"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print ("Fetching weather data from WeatherStack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return (response.json())

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        raise

def mock_fetch_data():
    print("Mock fetching weather data...")
    mock_response = {
        "request": {
            "type": "City",
            "query": "New York, United States of America",
            "language": "en",
            "unit": "m"
        },
        "location": {
            "name": "New York",
            "country": "United States of America",
            "region": "New York",
            "lat": "40.714",
            "lon": "-74.006",
            "timezone_id": "America/New_York",
            "localtime": "2024-06-01 12:00",
            "localtime_epoch": 1712102400,
            "utc_offset": "-4.0"
        },
        "current": {
            "temperature": 25,
            "weather_descriptions": ["Partly cloudy"],
            "wind_speed": 10,
            "humidity": 60
        }
    }
    return mock_response
