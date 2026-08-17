import requests
from dotenv import load_dotenv
import os
from cache.redis_cache import get_cache, set_cache
from fastapi import HTTPException
load_dotenv()

def get_weather(city):
    chave_api = os.getenv("API_KEY")
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"
    parametros = {
                "unitGroup": "metric",
                "key": chave_api,
                "contentType": "json"
    }
    cached_weather = get_cache(city)

    if cached_weather:
        return cached_weather

    try:
        response = requests.get(url, params=parametros, timeout=5)

    except requests.exceptions.RequestException:

        return {
            "error": "Failed to connect to the weather API"
        }

    if response.status_code == 200:

        weather_data = response.json()
        current_weather = weather_data.get("currentConditions", {})

        result = {
            "city": weather_data.get('address'),
            "temperature": current_weather.get('temp'),
            "temp_max": weather_data["days"][0].get('tempmax'),
            "temp_min": weather_data["days"][0].get('tempmin'),
            "feels_like": current_weather.get('feelslike'),
            "conditions": current_weather.get('conditions')
        }

        set_cache(city, result)

        return result

    elif response.status_code == 400:

        raise HTTPException(
            status_code=400,
            detail="Invalid city name"
        )

    elif response.status_code == 401:

        return {
            "error": "Invalid API Key",
            "status_code": response.status_code
        }

    elif response.status_code == 429:

        return {
            "error": "Too many requests",
            "status_code": response.status_code
        }

    elif response.status_code == 500:

        return {
            "error": "Internal Server Error",
            "status_code": response.status_code
        }
    else:

        return {
            "error": "Unexpected error",
            "status_code": response.status_code
        }
